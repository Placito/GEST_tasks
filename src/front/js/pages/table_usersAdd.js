import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Table_u } from "../component/table_u";

export const Table_usersAdd = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="container mt-5">
			<h1>Add users:</h1>
				<Table_u />
		</div>
	);
};
