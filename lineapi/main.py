from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FollowEvent
import os
import re
import requests
import json
import datetime

app = Flask(__name__)
BASEURL = "https://line-chore.herokuapp.com/"
START_TIME = ""

# 環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = "KiDr/tiz91H84JXNrClxJznm4WNhlkjiOoatl01/qJBoFKijBeoD8Exujazh50YqB9wVraLff81x4aYX/kS2HsIjnDk4JQuEL7/GiGq2nLZDLPUwIO2HUlSJ6+RkzI2c62BOD3iJ1VeyfDT+QGnDbwdB04t89/1O/w1cDnyilFU="
YOUR_CHANNEL_SECRET = "7dd35c1bc01470c8635a8059e8f6a64a"

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"


@app.route("/healthcheck", methods=["GET"])
def health_check():
    return {"message": "Hello!"}


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    line_id = profile.user_id  # -> ユーザーID

    if re.fullmatch(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", event.message.text):
        mail = event.message.text
        print(mail, line_id)

        payload = {"line_id": line_id, "email": mail}
        requests.post(BASEURL + "line_id", json=payload)

        line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text="ご協力ありがとうございます！")
    )

    elif event.message.text == "家事をする":
        payload = {"line_id": line_id}
        r = requests.get(BASEURL + "line/chores", json=payload).text
        chores_dict = json.loads(r)

        line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text='どの家事をやりますか？\n' + "\n".join(chores_dict.values()))
        )

    elif "start" in event.message.text:
        chore = event.message.text.split(" ")[0]
        start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        payload = {"line_id": line_id, "name": chore, "start": start_time}
        requests.post(BASEURL + "start", json=payload).text

        line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text="頑張ってください！")
        )

    elif "finish" in event.message.text:
        chore = event.message.text.split(" ")[0]
        finish_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        payload = {"line_id": line_id, "name": chore, "finish": finish_time}
        r = requests.post(BASEURL + "finish", json=payload).text

        time_dic = json.loads(r)
        name = time_dic["name"]
        start = datetime.datetime.strptime(time_dic["start"], '%Y-%m-%d %H:%M:%S')
        finish = datetime.datetime.strptime(time_dic["finish"], '%Y-%m-%d %H:%M:%S')

        timedelta = str(round((finish - start).seconds / 60))

        line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text="お疲れ様でした！\n" + timedelta + "分で「" + name + "」を終わらすことができました！")
        )

    else:

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text="家事を始めるには「家事をする」と入力してください。")
        )


@handler.add(FollowEvent)
def handle_follow(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    line_id = profile.user_id  # -> ユーザーID

    line_bot_api.reply_message(event.reply_token, TextSendMessage(text="こんにちは！認証のためにRAKU家事に登録したメールアドレスを送信してください！"))



