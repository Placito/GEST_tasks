import React, { useState, useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/table.css";

export const Table_p = () => {
	const { store, actions } = useContext(Context);
	const [newTask, setNewTask] = useState("");
	const [task, setTask] = useState(["Make the bed", "Wash my hands"]);

	// Get the value of a input when press the key Enter
	const handleKeyDown = event => {
		if (event.key === 'Enter') {
			setTask(task.concat(newTask)) 
			setNewTask("");
		}}
	
	//function for removing the element when the task is done
	const removeTodo = (currentIndex) => {
		setList((list.filter((element) => element !== currentIndex)));

		fetch(`https://jsonplaceholder.typicode.com/todos/${currentIndex}`, {
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
				<table className="table table-hover table-box" onKeyDown={handleKeyDown} onChange={e => setNewTask(e.target.value)} value={newTask} id="add-tasks" >
					<thead className="header-table">
						<tr>
						<th scope="col">Id's product</th>
						<th scope="col">Name</th>
						<th scope="col">Type</th>
						<th scope="col">Material</th>
						<th scope="col">Creation date</th>
						<th scope="col">Manufacturer</th>
						<th scope="col">Price</th>
						<th scope="col">Delete</th>
						</tr>
					</thead>
					<tbody>
						<tr>
						<th scope="row">1</th>
						<td>Mark</td>
						<td>Otto</td>
						<td>@mdo</td>
						<td>@mdo</td>
						<td>@mdo</td>
						<td>@mdo</td>
						<th>Last update:</th>
						<td><i className="fa-solid fa-trash-can"></i></td>
						</tr>
						<tr>
						<th scope="row">2</th>
						<td>Jacob</td>
						<td>Thornton</td>
						<td>@fat</td>
						<td>@mdo</td>
						<td>@mdo</td>
						<td>@mdo</td>
						<th>Last update:</th>
						<td><i className="fa-solid fa-trash-can"></i></td>
						</tr>
					</tbody>
				</table>
		</div>
	);
};
