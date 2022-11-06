import React from "react";
import { useForm, SubmitHandler } from 'react-hook-form';
import { ErrorMessage } from '@hookform/error-message';
import "./Top.css"
import { Link } from "react-router-dom";
import appImage from "../images/logo-red.png";

type Inputs = {
  name: string;
  category: string;
  interval: number;
  interval_unit: string;
};

export const ChoreEdit: React.FC = () => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm<Inputs>();

  const onSubmit: SubmitHandler<Inputs> = (data) => {
    console.log(data);
    reset();
  };

  const deleteElement=() => {
    console.log("delete element");
    reset();
  }

  return (
    <div>
      <div className="header">
        <div className="flex_test-item"><img src={appImage} alt="app-logo"/></div>
        <div className="flex_test-item"><h1>家事情報の変更</h1></div>
      </div>
      <hr/>
      <div className="Top">
        <form onSubmit={handleSubmit(onSubmit)}>
          <p className="category-name">家事名</p>
          <input
            {...register('name', {
              required: '家事名を入力してください',
            })}
            defaultValue="元の家事名"
            className="input-field"
          />
          <ErrorMessage errors={errors} name="name" />
          <p className="category-name">カテゴリー</p>
          <select
            {...register('category', {
              required: 'カテゴリーを選択してください',
            })}>
            <option value="clean">そうじ</option>
            <option value="eat">食事</option>
            <option value="trash">ゴミ</option>
          </select>
          <ErrorMessage errors={errors} name="category" />
          <p className="category-name">周期</p>
          <input
            {...register('interval', {
              required: '周期を入力してください',
            })} 
            type='number'
            defaultValue="1"
            className="input-field"
          />
          <select {...register("interval_unit", {
            required: '周期を入力してください'
          })}>
            <option value="hour">時間</option>
            <option value="day" selected>日</option>
            <option value="week">週</option>
            <option value="month">月</option>
          </select>
          <ErrorMessage errors={errors} name="interval" />
          <div className="top-btn">
            <p><Link to="/chores"><button type="submit">変更する</button></Link></p>
          </div>
          <div className="delete-btn">
            <p><Link to="/chores"><button onClick={deleteElement}>削除する</button></Link></p>
          </div>
        </form>
      </div>
    </div>
  );
};
