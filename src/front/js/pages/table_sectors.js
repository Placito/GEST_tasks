import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Table_p } from "../component/table_p";

export const Table_sectors = () => {
	const { store, actions } = useContext(Context);
	const [task, setTask] = useState(["Check the task's", "Feed the cattle"]);

	return (
		<div className="container mt-5">
			<h1>Consult:</h1>
			{task.map(item => (
				<Table_p text={item} removeTodo = {removeTodo} />
				))}
		</div>
	);
};
