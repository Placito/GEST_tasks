import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Table_u } from "../component/table_u";

export const Table_users = () => {
	const { store, actions } = useContext(Context);
	const [task, setTask] = useState(["Check the task's", "Feed the cattle"]);

	return (
		<div className="container mt-5">
			<h1>Consult users:</h1>
			{task.map(item => (
				<Table_u text={item} removeTodo = {removeTodo} />
				))}
		</div>
	);
};
