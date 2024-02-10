import React, { useState, useContext } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";
import axios from 'axios';
import "../../styles/table.css";

export const AddUser = () => {
    const { store, actions } = useContext(Context);
    const [formData, setFormData] = useState({
            username: '',
            email: '',
            password: '',
            role: ''
        });
    
        const handleChange = (e) => {
            setFormData({ ...formData, [e.target.name]: e.target.value });
        };
    
        const handleSubmit = async (e) => {
            e.preventDefault();
            try {
                const response = await axios.post('/create-user', formData);
                console.log(response.data.message);
                // Reset form after successful submission
                setFormData({
                    username: '',
                    email: '',
                    password: '',
                    role: ''
                });
            } catch (error) {
                console.error('Error creating user:', error.response.data.error);
            }
        };

	return (
		<div className="container">
            <h1>Add a new User:</h1>
			<form onChange={(e) => handleChange(e)} onSubmit={handleSubmit}>
                <div className="mb-3 row">
                    <input type="text" value={formData.username} className="form-control" name="username" placeholder="Enter username" />
                </div>
                <div className="mb-3 row">
                    <input type="email" value={formData.email} className="form-control" name="email" placeholder="Enter email" />
                </div>
                <div className="mb-3 row">
                    <input type="text" value={formData.role} className="form-control" name="role" placeholder="Enter role" />
                </div>
                <div className="mb-3 row">
                    <input type="password" value={formData.password} className="form-control" name="password" placeholder="Enter password" />
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