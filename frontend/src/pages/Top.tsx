import React from "react";
import { Link } from "react-router-dom";
import { useForm, SubmitHandler } from 'react-hook-form';
import { ErrorMessage } from '@hookform/error-message';
import "./Top.css"
import appImage from "../images/app-logo.png";

type Inputs = {
  email:string;
  password:string;
};

export const Top: React.FC = () => {

  const {
    register,
    handleSubmit,
    reset,
    formState:{errors},
  } = useForm<Inputs>({
    mode: "onChange",
    criteriaMode: "all",
    shouldFocusError: false,
  });

  const onSubmit:SubmitHandler<Inputs> = (data) =>{
    console.log(data);
    reset();

  };

  return (
    <>
    <div className="background">
      <div className="app-logo"><img src={appImage} alt="app-logo"/></div>
    </div>

    <div className="Top">
      <form onSubmit={handleSubmit(onSubmit)}>
        <p className="category-name">メールアドレス</p>
          <br/>
          <input
              {...register('email',{
                  required: true,
                  maxLength:60,
                  pattern:/^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$/,
                })} 
                  type="email" 
                  id="email" 
                  className="input-field"
          />
          <br/>
          {errors.email?.types?.required && "メールアドレスが長すぎます"}
          {errors.email?.types?.pattern && "メールアドレスの形式が不正です"}
          <br/>

        <p  className="category-name">パスワード</p> 
          <br/>
          <input 
              {...register('password',{
                  required:'パスワードを入力してください',
                  minLength:8,
                  maxLength:100
                })}
                  type="password" 
                  id="password" 
                  className="input-field"
          />
          <br/>
          {errors.password?.types?.required && "パスワードを入力してください"}
          {errors.password?.types?.minLength && "パスワードは8文字以上で入力してください"}
          {errors.password?.types?.maxLength && "パスワードは100文字以下で入力してください"}
          <br/>

        <div className="top-btn">
          <p><Link to="/chores"><button type="submit">ログイン</button></Link></p>
          <p><Link to="/user/signup"><button type="submit">新規登録</button></Link></p>
        </div>
      </form>
    </div>
    </>
  );
};
