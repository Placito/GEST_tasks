import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";

export const Table_sectors = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="text-center mt-5">
			<h1>Hello Rigo!!</h1>
			
		</div>
	);
};
