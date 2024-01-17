import React, { useState, useEffect, useContext } from "react";
import { Link, useParams } from "react-router-dom";
import { Context } from "../store/appContext";

export const EditUser = () => {
    const { store, actions } = useContext(Context);
    const params = useParams(); 
	const [user, setUser] = useState({
		username: "",
		name: "",
		role: "",
        password: ""
	});
	
   function onChangeForm(e) {
        user[e.target.id] = e.target.value
        setUser(user)
            
        console.log(e.target.value) 
    }
    
    useEffect (() => {
        if (store.users && store.users.length > 0 && store.users[params.index]) {
            setUser(store.users[params.index]) 
        }
    }, [store.users])

	return (
		<div className="container">
            <h1>Edit Contact:</h1>
			<form onChange={(e) =>  onChangeForm(e)} onSubmit={(e) => e.preventDefault()}>
                <div className="mb-3 row">
                    <input type="text" className="form-control" id="username" placeholder="Enter username" />
                </div>
                <div className="mb-3 row">
                    <input type="name" className="form-control" id="name" placeholder="Enter name" />
                </div>
                <div className="mb-3 row">
                    <input type="text"  className="form-control" id="role" placeholder="Enter role" />
                </div>
                <div className="mb-3 row">
                    <input type="text" className="form-control" id="password" placeholder="Enter password" />
                </div>
                <Link className="link-user" to="/table_users">
                    <div className="row"> 
                        <button type="submit" onClick={() => actions.update(user)} className="btn-user" >Edit</button>
                    </div>
                </Link>
                <br /> 
                <Link className="link-user" to="/table_users">or get back to tables</Link>
            </form>
		</div>
	);
};