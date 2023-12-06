import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Table_u } from "../component/table_u";

export const Table_usersAdd = () => {
	const { store, actions } = useContext(Context);
	const [task, setTask] = useState(["Check the task's", "Feed the cattle"]);
	
	return (
		<div className="container mt-5">
			<h1>Add users:</h1>
			{task.map(item => (
				<Table_u text={item}/>
				))}
		</div>
	);
};
