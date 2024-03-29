import React, { useState, useEffect, useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/table.css";
import { Link } from "react-router-dom";
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
		setUser((actions.users.filter((element) => element !== currentIndex)));

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

	// Get the value of a input when press the key Enter
	const handleKeyDown = event => {
		if (event.key === 'Enter') {
			setUser(user.concat(user)) 
			setUser("");

		fetch('https://randomuser.me/api/${currentIndex}', {
				method: 'POST',
				body: JSON.stringify(user),
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
		};
	}

	return (
		<div className="container mt-5">
				<table className="table table-hover table-box" onKeyDown={handleKeyDown} onChange={e => setUser(e.target.value)} value={user} id="add-task">
					<thead className="header-table">
						<tr>
						<th className="text-center" scope="col">Id</th>
						<th className="text-center" scope="col">Name</th>
						<th className="text-center" scope="col">Role</th>
						<th className="text-center" scope="col">Username</th>
						<th className="text-center" scope="col">Password</th>
						<th className="text-center" scope="col">Delete</th>
						<th className="text-center" scope="col">Edit</th>
						</tr>
					</thead>
					<tbody>
						<tr>
						<th className="text-center" scope="row">{props.index}</th>
						<td className="text-center">{props.contact.name.first}</td>
						<td className="text-center">{props.contact.login.salt}</td>
						<td className="text-center">{props.contact.login.username}</td>
						<td className="text-center">{props.contact.login.password}</td>
						<td className="text-center"><i className="fa-solid fa-trash-can" onClick={() => props.removeUser()}></i></td>
						<td className="text-center">
							<Link to={"/editUser/" + props.index}><i className="fa-solid fa-pen-to-square icon"></i></Link>
						</td>
						</tr>
					</tbody>
				</table>
				<Link to="/addUser">
					<button className="btn-user">Add a User</button>
				</Link>
		</div>
	);
};
