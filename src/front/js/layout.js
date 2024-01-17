import React, { useEffect, useState } from 'react';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";
import { BackendURL } from "./component/backendURL";
import { UserProvider } from './component/userContext';
import SelectedTypeContext from './TypeContext';
import { Details_Home } from "./pages/details_Home";
import { Details_Sectors } from "./pages/details_Sectors";
import { Login } from "./pages/login";
import { Choose_1 } from "./pages/choose_1";
import { Choose_2 } from "./pages/choose_2";
import { Choose_3 } from "./pages/choose_3";
import { Table_sectors } from "./pages/table_sectors";
import { Table_users } from "./pages/table_users";
import { AddUser } from "./component/addUser";
import { EditUser } from "./component/editUser";
// import { Chatbot } from "./pages/chatbot";
import injectContext from "./store/appContext";

import { Navbar } from "./component/navbar";

//create your first component
const Layout = () => {
    //the basename is used when your project is published in a subdirectory and not in the root of the domain
    // you can set the basename on the .env file located at the root of this project, E.g: BASENAME=/react-hello-webapp/
    const basename = process.env.BASENAME || "";
    const [selectedType, setSelectedType] = useState('');
    if(!process.env.BACKEND_URL || process.env.BACKEND_URL == "") return <BackendURL/ >;

    return (
        <div>
            <UserProvider>
            <SelectedTypeContext.Provider value={{ selectedType, setSelectedType }}>
            <BrowserRouter basename={basename}>
                <ScrollToTop>
                    <Navbar />
                    <Routes>
                        <Route element={<Details_Home />} path="/" />
                        <Route element={<Login />} path="/login" />
                        <Route element={<Details_Sectors />} path="/Details_Sectors" />
                        <Route element={<Choose_1 />} path="/choose_1" />
                        <Route element={<Choose_2 />} path="/choose_2" />
                        <Route element={<Choose_3 />} path="/choose_3" />
                        <Route element={<Table_sectors />} path="/table_sectors" />
                        <Route element={<Table_users />} path="/table_users" />
                        <Route element={<AddUser />} path="/addUser" />
                        <Route element={<EditUser />} path="/editUser" />
                        <Route element={<h1>Not found!</h1>} />
                    </Routes>
                </ScrollToTop>
            </BrowserRouter>
            </SelectedTypeContext.Provider>
            </UserProvider>
        </div>
    );
};

export default injectContext(Layout);
