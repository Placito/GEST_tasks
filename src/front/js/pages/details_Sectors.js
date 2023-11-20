import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Sectors } from "../component/sectors";

export const Details_Sectors = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="text-center mt-5">
			<Sectors />
		</div>
	);
};
