import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Table_p } from "../component/table_p";

export const Table_sectors = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="container mt-5">
			<h1>Consult:</h1>
				<Table_p />
		</div>
	);
};
