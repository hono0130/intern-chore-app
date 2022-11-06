import React from 'react';
import './App.css';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Top } from "./pages/Top";
import { ChoreList } from "./pages/ChoreList";
import { ChoreEdit } from "./pages/ChoreEdit";
import { ChoreCreate } from "./pages/ChoreCreate";
import { SignUp } from "./pages/SignUp";
import { UserEdit } from "./pages/UserEdit";
import { Header } from "./components/Header";

function App() {
  return (
    <BrowserRouter>
      {/* <Header /> */}
      <Routes>
        <Route path={"/"} element={<Top />} />
        <Route path={"/chores"}>
          <Route index element={<ChoreList />} />
          <Route path={":id/edit"} element={<ChoreEdit />} />
        </Route>
        <Route path={"/chores/new"} element={<ChoreCreate />} />
        <Route path={"/user/signup"} element={<SignUp />} />
        <Route path={"/user/:id/edit"} element={<UserEdit />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
