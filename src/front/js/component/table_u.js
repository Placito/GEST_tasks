import React, { useState, useEffect, useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/table.css";
import { useParams } from "react-router-dom";

export const Table_u = (props) => {
	const { store, actions } = useContext(Context);
	const params = useParams();
	const [user, setUser] = useState({
		username: "",
		namel: "",
		role: "",
        password: ""
	});

	useEffect(() => {
		if (params.id) {
			actions.getUsersById(params.id);
		}}, []);
	
	//function for removing a user
	const removeUser = (currentIndex) => {
		setList((list.filter((element) => element !== currentIndex)));

		fetch(`https://randomuser.me/api/${currentIndex}`, {
			method: 'DELETE',
			headers:{
				'Content-Type': 'application/json'
			}
		})
		.then(res => {
			if (!res.ok) throw Error(res.statusText);
			return res.json();
		})
		.then(response => console.log('Success:', response))
		.catch(error => console.error(error));
	}

	return (
		<div className="container mt-5">
				<table className="table table-hover table-box" onKeyDown={handleKeyDown} onChange={e => setUser(e.target.value)} value={user} id="add-task">
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
						<td><i className="fa-solid fa-trash-can" onClick={ () => removeUser()}></i></td>
						</tr>
					</tbody>
				</table>
		</div>
	);
};
