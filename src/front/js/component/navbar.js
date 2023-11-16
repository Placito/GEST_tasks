import React from "react";
import { Link } from "react-router-dom";
import logo from "../../img/logo.png";
import "../../styles/navbar.css";

export const Navbar = () => {
	return (
		<nav className="navbar navbar-expand-lg navbar-box">
			<div className="container-fluid">
				<div className="d-flex">
					<Link  to="/">
						<img src={logo} className="img" alt="logo" />
					</Link>
					<p className="task-paragraf">Task managemnet software</p>
				</div>
				<form className="d-flex">
					<button className="btn-logout" type="submit">Logout</button>
				</form>
			</div>
		</nav>
	);
};
