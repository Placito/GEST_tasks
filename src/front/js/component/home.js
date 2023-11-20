import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";
import "../../styles/home.css";

export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="container mt-5">
			<h1>Choose your role:</h1>
			<div className="roles-box mt-5">
				<Link  to="/login">
					<div className="card card-1" style={{ width: "20rem" }}>
						<p>Director</p>
					</div>
				</Link>	
				<Link  to="/login">
					<div className="card card-2" style={{ width: "20rem" }}>
						<p>Administrative</p>
					</div>
				</Link>
				<Link  to="/login">
					<div className="card card-3" style={{ width: "20rem" }}>
						<p>Techinician</p>
					</div>
				</Link>	
			</div>
			<div className="roles-box mt-5">
				<Link  to="/login">
					<div className="card card-4" style={{ width: "20rem" }}>
						<p>Operator</p>
					</div>
				</Link>	
					<Link  to="/login">
					<div className="card card-5" style={{ width: "20rem" }}>
						<p>Quality Controler</p>
					</div>
				</Link>	
			</div>
		</div>
	);
};
