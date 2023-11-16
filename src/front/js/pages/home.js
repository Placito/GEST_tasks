import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";

export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="container mt-5">
			<h1>Choose your role:</h1>
			<div className="roles-box mt-5">
				<div className="card" style={{ width: "60rem" }}>
					<img src="..." className="card-img-top" alt="..." />
					<p>Director</p>
				</div>
				<div className="card" style={{ width: "60rem" }}>
					<img src="..." className="card-img-top" alt="..." />
					<p>Administrative</p>
				</div>
				<div className="card" style={{ width: "60rem" }}>
					<img src="..." className="card-img-top" alt="..." />
					<p>Techinician</p>
				</div>
			</div>
			<div className="roles-box mt-5">
				<div className="card" style={{ width: "60rem" }}>
					<img src="..." className="card-img-top" alt="..." />
					<p>Operator</p>
				</div>
				<div className="card" style={{ width: "60rem" }}>
					<img src="..." className="card-img-top" alt="..." />
					<p>Quality Controler</p>
				</div>
			</div>
		</div>
	);
};
