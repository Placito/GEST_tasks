import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/table.css";

export const Table_u = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="container mt-5">
				<table className="table table-hover table-box">
					<thead className="header-table">
						<tr>
						<th scope="col">Id's user</th>
						<th scope="col">Username</th>
						<th scope="col">Name</th>
						<th scope="col">Role</th>
						<th scope="col">Delete</th>
						</tr>
					</thead>
					<tbody>
						<tr>
						<th scope="row">1</th>
						<td>Mark</td>
						<td>Otto</td>
						<td>@mdo</td>
						<td><i className="fa-solid fa-trash-can"></i></td>
						</tr>
						<tr>
						<th scope="row">2</th>
						<td>Jacob</td>
						<td>Thornton</td>
						<td>@fat</td>
						<td><i className="fa-solid fa-trash-can"></i></td>
						</tr>
					</tbody>
				</table>
		</div>
	);
};
