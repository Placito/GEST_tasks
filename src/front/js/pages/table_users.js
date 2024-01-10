import React, { useEffect, useContext } from "react";
import { Context } from "../store/appContext";
import { Table_u } from "../component/table_u";
import { useParams } from "react-router-dom";

export const Table_users = () => {
	const { store, actions } = useContext(Context);
	const params = useParams();

	// fetch users API
	useEffect(() => {
			actions.getUsers();
	}, []);

	return (
		<div className="container mt-5">
			<h1>Consult users:</h1>
			{store.users.map(item => (
				<Table_u text={item} />
				))}
		</div>
	);
};
