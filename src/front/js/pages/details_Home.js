import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";
import { Home } from "../component/home";

export const Details_Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="container mt-5">
			<Home />
		</div>
	);
};
