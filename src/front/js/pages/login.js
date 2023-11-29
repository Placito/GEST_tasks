import React, { useState, useEffect, useContext } from "react";
import "../../styles/login.css";
import { Link, useNavigate } from "react-router-dom";
import { Context } from "../store/appContext";

export const Login = () => {
	const { store, actions } = useContext(Context);
	const [username, setUsername] = useState("");
	const [password, setPassword] = useState("");
	const navigate = useNavigate();

	const handleClick = () => {

		const opts = {
			method: 'POST',
			headers: {
				"content-Type": "application/json"
			},
			body: JSON.stringify({
				"username": username,
				"passsword": password
			})
		}
		fetch(process.env.BACKEND_URL + '/api/token', opts)
		.then(resp => {
			console.log(resp)
			if(resp.status === 200) return resp.json();
			else alert("There has been some error");
		})
		.then(data => {
			sessionStorage.setItem("token", data.access_token);
		})
		.catch(error => {
			console.error(error);
		})
	}
	return (
		<div className="container">
			<h4 className="text-login">Login to your account:</h4>
			<div >
			  <br />
			  <div className="form-outline mb-4">
				<input
				  type="text"
				  className="form-control-lg form-input-login"
				  placeholder="Username"
				  value = {username}
				  onChange={(e) => setUsername(e.target.value)}
				  required
				/>
			  </div>
			  <div className="form-outline mb-4">
				<input
				  type="password"
				  className="form-control-lg form-input-login"
				  placeholder="Password"
				  value = {password}
				  onChange={(e) => setPassword(e.target.value)}
				  required
				/>
			  </div>
			  <div className="form-check d-flex row mt-4 p-0 ms-0">
				<div className="d-flex ">
				  <div className=" d-flex col-6 ">
					<input
					  className="form-check-input-login me-2"
					  type="checkbox"
					  value=""
					  id="form1Example3"
					/>
					  <label className="form-check-label remember" htmlFor="form1Example3">
						{" "}
						Remember password{" "}
					  </label>
				</div>
				<Link
				  className="forgot-link link col-6"
				  to="/resetPassword"
				  type="submit"
				>
				  Forgot Password?
				</Link>
			  </div>
			  </div>
			  <br/>
			  <br/>
			  <br/>
			  <br/>
			  <div className="text-center">
				<button
				  className="btn-login"
				  onClick={handleClick}
				>
				  Login
				</button>
			  </div>
			</div>
		  </div>
	);
};
