import React, { useState, useEffect, useContext } from "react";
import "../../styles/login.css";
import { Link, useParams } from "react-router-dom";
import { Context } from "../store/appContext";

export const Login = () => {
	const { store, actions } = useContext(Context);
	const params = useParams();

	return (
		<div className="container">
			<h4 className="text-login">Login to your account:</h4>
			<div >
			  <br />
			  <div className="form-outline mb-4">
				<input
				  type="email"
				  id="typeEmailX-2"
				  className="form-control-lg form-input-login"
				  placeholder="Username"
				  required
				/>
			  </div>
			  <div className="form-outline mb-4">
				<input
				  type="password"
				  id="typePasswordX"
				  className="form-control-lg form-input-login"
				  placeholder="Password"
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
				>
				  Login
				</button>
			  </div>
			</div>
		  </div>
	);
};
