import React from "react";
import { useNavigate } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import Card from 'react-bootstrap/Card';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import appImage from "../images/logo-red.png";
import logoutImage from "../images/logout.jpeg";
import userImage from "../images/user.jpeg";

export const ChoreList: React.FC = () => {
  const [startDate, setStartDate] = React.useState<string>(formatDate(new Date()));
  const [finishDate, setFinishDate] = React.useState<string>(formatDate(new Date()));
  const navigate = useNavigate();

  // todoかdoneかのフラグステート
  const [todo, setTodo] = React.useState<boolean>(true);

  // 実行中かどうかのフラグステート
  const [doing, setDoing] = React.useState<boolean>(false);

  // startボタンをクリックした際の処理
  function pushStart() {
    setDoing(true);
    setStartDate(formatDate(new Date()));
  };

  // finishボタンをクリックした際の処理
  function pushFinish() {
    setDoing(false);
    setFinishDate(formatDate(new Date()));
  };

  // TODOの家事かDONEの家事かの表示切替
  const card = (todo: boolean) => {
    if (todo) {
      return <TodoCard />;
    } else {
      return <DoneCard />;
    };
  };

  // 家事を実行中かどうかで表示するボタンの切り替え
  const button = (doing: boolean) => {
    if (doing) {
      return <FinishButton onClick={() => pushFinish()} />;
    } else {
      return <StartButton onClick={() => pushStart()} />;
    };
  };

  // 日時を適切なデータ型にフォーマットする関数
  function formatDate(date: Date) {
    const y = date.getFullYear();
    const m = ("00" + (date.getMonth() + 1)).slice(-2);
    const d = ("00" + date.getDate()).slice(-2);
    return y + "-" + m + "-" + d;
  }

  // 画面描画内容
  return (
    <div>
      <div className="header">
        <div className="flex_test-item"><img src={appImage} alt="app-logo"/></div>
        <div className="flex_test-item"><h1>家事一覧</h1></div>
        <div className="flex_test-item"><img src={userImage} height="120" onClick={() => navigate("/user/1/edit")}/></div>
        <div className="flex_test-item"><img src={logoutImage} height="120" onClick={() => navigate("/")}/></div>
      </div>
      <hr/>
      <Row className="justify-content-md-center">
        <ButtonGroup aria-label="Basic example">
          <Button onClick={() => (setTodo(true))} variant="outline-danger" >TODO</Button>
          <Button onClick={() => (setTodo(false))} variant="outline-danger" >DONE</Button>
        </ButtonGroup>
      </Row>
      <br />
      <Row className="justify-content-md-center">
        {/* {offerings.map((a) => ( */}
        <Card style={{ width: '18rem' }}>
          <Card.Img variant="top" src="holder.js/100px180" />
          <Card.Body>
            <div onClick={() => navigate("/chores/1/edit")}>
              <Card.Title>Card Title</Card.Title>
              <Card.Text >
                {card(todo)}
              </Card.Text>
            </div>
            {button(doing)}
          </Card.Body>
        </Card>
        <br />
        {/* ))} */}
        <br />
        <Button variant="danger" style={{ width: '18rem' }} onClick={() => navigate("/chores/new")} > + </Button>
      </Row>
    </div>
  );
};

// TODOの家事を表示するためのカード
const TodoCard: React.FC<{}> = ({ }) => {
  return (
    <>
      <p>家事の名前</p>
      <p>前回から3日経過</p>
    </>
  );
};

// DONEの家事を表示するためのカード
const DoneCard: React.FC<{}> = ({ }) => {
  return (
    <>
      <p>家事の名前</p>
      <p>前回から4日経過</p>
    </>
  );
};

// 家事開始ボタン
const StartButton: React.FC<{ onClick: () => void }> = ({ onClick }) => {
  return (
    <Button onClick={onClick} variant="danger" style={{ width: '14rem' }}>
      start
    </Button>
  );
};

// 家事終了ボタン
const FinishButton: React.FC<{ onClick: () => void }> = ({ onClick }) => {
  return (
    <Button onClick={onClick} variant="success" style={{ width: '14rem' }}>
      finish
    </Button>
  );
};
