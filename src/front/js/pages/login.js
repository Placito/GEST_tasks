import React, { useState } from "react";
import "../../styles/login.css";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { useUser } from "../component/userContext";

export function Login() {
	const [username, setUsername] = useState("");
	const [password, setPassword] = useState("");
	const navigate = useNavigate();
	const [usernameFlag, setUsernameFlag] = useState(false);
	const [passwordFlag, setPasswordFlag] = useState(false);
	const [apiFlag, setAPIFlag] = useState(false);
	const [message, setMessage] = useState("Wrong credential");
	const { setIsLoggedIn } = useUser(false);

	async function login(event) {
		event.preventDefault();
		let flag = true;
		if (username === "") {
		  flag = false;
		  setUsernameFlag(true);
		}
		if (password === "") {
		  flag = false;
		  setPasswordFlag(true);
		}
		if (!flag) {
		  setMessage("Wrong credential");
		  return;
		}
			const payload = {
			username: username,
			password: password,
			};
			try {
			const response = await axios.post(process.env.BACKEND_URL + "/api/token", payload);
			console.log(response);
		
			if (response.data.success === "true") {
				// Store access token in local storage
				localStorage.setItem('access_token', response.data.access_token);
				//console.log("Login successful");
				console.log("Stored Token: ", localStorage.getItem('access_token'));
				//console.log(localStorage.getItem('access_token'));
		
				console.log("Navigating ..."); // to check if Navigation function is called
		
				if (localStorage.getItem('access_token')) {
				setIsLoggedIn(true);
				navigate("/details_Sectors");
		
				} else {
				console.log("Token not set");
				}
			} else {
				setAPIFlag(true);
				setMessage(response.data.msg);
				console.log("Login failed");
			}
			} catch (error) {
			if (error.response) {
				console.log(error.response);
			}
			}
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
				  id="typeUsernameX"
				  placeholder="Username"
				  value = {username}
				  onChange={(e) => setUsername(e.target.value)}
				  required
				/>
			  </div>
			  <div className="form-outline mb-4">
				<input
				  type="password"
				  id="typePasswordX"
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
			  </div>
			  </div>
			  <br/>
			  <br/>
			  <br/>
			  <br/>
			  {usernameFlag || apiFlag || passwordFlag ? (
                  <p className="text-danger">{message}</p>
                ) : null}
			  <div className="text-center">
				<button
				  className="btn-login"
				  onClick={login}
				>
				  Login
				</button>
			  </div>
			</div>
		  </div>
	);
}
