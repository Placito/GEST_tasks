import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/choose.css";

export const Choose_3 = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="container mt-5">
			<div className="box mt-5">
				<div className="title">
					<h1>These are the function you can perform:</h1>
				</div>
				<div className="buttons">
					<button className="btn-tasks" type="submit">Consult Users</button>
					<button className="btn-tasks" type="submit">Add/Delet Users</button>
					<button className="btn-tasks" type="submit">Consult Sectors</button>
				</div>
			</div>
			<div className="set-arrow">
				<div className="legend-arrow" >Go Back</div>
				<div className="btn-arrow" type="submit"><i className="fa-solid fa-arrow-left"></i></div>
			</div>
			
		</div>
	);
};
