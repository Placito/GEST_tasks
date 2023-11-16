import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";

export const Choose_3 = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="text-center mt-5">
			<h1>Hello Rigo!!</h1>
			
		</div>
	);
};
