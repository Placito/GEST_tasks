import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";
import "../../styles/home.css";

export const Sectors = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="container mt-5">
			<h1>Choose your role:</h1>
			<div className="roles-box mt-5">
				<Link  to="/login">
					<div className="card card-1" style={{ width: "20rem" }}>
						<p>Sector_1</p>
					</div>
				</Link>	
				<Link  to="/login">
					<div className="card card-2" style={{ width: "20rem" }}>
						<p>Sector_2</p>
					</div>
				</Link>
				<Link  to="/login">
					<div className="card card-3" style={{ width: "20rem" }}>
						<p>Sector_3</p>
					</div>
				</Link>	
			</div>
			<div className="roles-box mt-5">
				<Link  to="/login">
					<div className="card card-4" style={{ width: "20rem" }}>
						<p>Sector_4</p>
					</div>
				</Link>	
				<Link  to="/login">
					<div className="card card-5" style={{ width: "20rem" }}>
						<p>Sector_5</p>
					</div>
				</Link>	
                <Link  to="/login">
					<div className="card card-5" style={{ width: "20rem" }}>
						<p>Sector_6</p>
					</div>
				</Link>	
			</div>
		</div>
	);
};
