import React, { useState, useContext } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";
import "../../styles/table.css";

export const AddUser = () => {
    const { store, actions } = useContext(Context);

    //function to change the value from on an specific id of an input an assing it to a new object
    function onChangeForm(e) {
        const { id, value } = e.target;
        console.log({id, value});
    }

	return (
		<div className="container">
            <h1>Add a new User:</h1>
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
                        <button type="submit" onClick={() => actions.addUser(store.users)} className="btn-user" >Save</button>
                    </div>
                </Link>
                <br /> 
                <Link className="link-user" to="/table_users">or get back to tables</Link>
            </form>
		</div>
	);
};