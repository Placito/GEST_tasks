import React, { useState, useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import { Link, useParams, useNavigate } from "react-router-dom";
import axios from "axios";
import logo from "../../img/logo.png";
import "../../styles/navbar.css";
import LogoutComponent from "../component/logout";
import { useUser } from "../component/userContext";

export const Navbar = (token) => {
	const { store, actions } = useContext(Context);
  	const { isLoggedIn, setIsLoggedIn } = useUser(false);
	const params = useParams();
 	const navigate = useNavigate();

	  useEffect(() => {
		const token = localStorage.getItem('access_token');
	
		if (token) getData(token);
	
	  }, []); 
	
	  const getData = (token) => {
	
		axios({
		  method: "GET",
		  url: process.env.BACKEND_URL + "/profile",
		  headers: {
			Authorization: `Bearer ${token}`
		  },
		})
	
		  .then((response) => {
			const res = response.data;
			console.log("Profile Data:", res);
			console.log('Token in Profile:', token);
			actions.setUserProfile(res);
		  })
		  .catch((error) => {
			console.error("An error occurred in getData:", error);
			if (error.response) {
			  console.log("Error details:", error.response);
			}
		  });
	  }

	return (
		<nav className="navbar navbar-expand-lg navbar-box">
			<div className="container-fluid">
				<div className="d-flex">
					<Link  to="/">
						<img src={logo} className="img" alt="logo" />
					</Link>
					<p className="task-paragraf">Task managemnet software</p>
				</div>
				{ isLoggedIn ?
				<LogoutComponent onLogout={() => {
					actions.logout();
					setIsLoggedIn(false)
					navigate('/');
				  }} />
				: "" }
			</div>
		</nav>
	);
};
