import React from "react";
import { useForm, SubmitHandler } from 'react-hook-form';
import { ErrorMessage } from '@hookform/error-message';
import "./Top.css"
import { Link } from "react-router-dom";
import appImage from "../images/logo-red.png";

type Inputs = {
  email: string;
  username: string;
  password: string;
};

export const SignUp: React.FC = () => {
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

  return (
  <div>
    <div className="header">
      <div className="flex_test-item"><img src={appImage} alt="app-logo"/></div>
      <div className="flex_test-item"><h1>新規登録</h1></div>
    </div>
    <hr/>
    <div className="Top">
      <form onSubmit={handleSubmit(onSubmit)}>
          <p className="category-name">メールアドレス</p>
          <input
            {...register('email', {
              required: true,
              maxLength: {
                value: 100,
                message: 'メールアドレスが長すぎます'
              },
              pattern: {
                value:
                  /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$/,
                message: 'メールアドレスの形式が不正です',
              },
            })}
            className="input-field"
          />
          <ErrorMessage errors={errors} name="email" />
          <p className="category-name">ユーザー名</p>
          <input
            {...register('username', {
              required: 'ユーザー名を入力してください',
            })}
            className="input-field"
          />
          <ErrorMessage errors={errors} name="username" />
          <p className="category-name">パスワード</p>
          <input
            {...register('password', {
              required: 'パスワードを入力してください',
              minLength: {
                value: 8,
                message: 'パスワードは8文字以上で入力してください',
              },
              maxLength: {
                value: 100,
                message: 'パスワードは100文字以下で入力してください',
              }
            })}
            type="password"
            className="input-field"
          />
          <ErrorMessage errors={errors} name="password" />
          <div className="top-btn">
            <p><Link to="/"><button type="submit">登録する</button></Link></p>
          </div>
        </form>
      </div>
    </div>
  );
};
