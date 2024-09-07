import React, { useState, useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/table.css";

export const Table_p = () => {
    const { store, actions } = useContext(Context);
    const [newTask, setNewTask] = useState("");
    const [tasks, setTasks] = useState(["Make the bed", "Wash my hands"]); // Renamed to 'tasks'

    // Get the value of input when the Enter key is pressed
    const handleKeyDown = event => {
        if (event.key === 'Enter' && newTask.trim() !== "") {
            setTasks(tasks.concat(newTask));
            setNewTask("");
        }
    };

    // Function to handle task update
    const handleUpdate = (index) => {
        const updatedTask = prompt("Enter new task name: ", tasks[index]);
        if (updatedTask) {
            const updatedTasks = [...tasks];
            updatedTasks[index] = updatedTask;
            setTasks(updatedTasks);
            actions.update(index, updatedTask); // Ensure the 'update' action is defined in your flux
        }
    };

    // Function for removing the element when the task is done
    const removeTodo = (index) => {
        const updatedTasks = tasks.filter((_, taskIndex) => taskIndex !== index);
        setTasks(updatedTasks);

        // Assuming you would like to send a DELETE request as well
        fetch(`https://jsonplaceholder.typicode.com/todos/${index}`, {
            method: 'DELETE',
            headers: {
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

    return (
        <div className="container mt-5">
            <input 
                type="text"
                placeholder="Add new task"
                value={newTask}
                onChange={e => setNewTask(e.target.value)}
                onKeyDown={handleKeyDown}  // Move input-specific handlers to the input element
                className="form-control"
            />

            <table className="table table-hover table-box mt-3">
                <thead className="header-table">
                    <tr>
                        <th scope="col">Id</th>
                        <th scope="col">Task</th>
                        <th scope="col">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {tasks.map((task, index) => (
                        <tr key={index}>
                            <th scope="row">{index + 1}</th>
                            <td>{task}</td>
                            <td>
                                <button onClick={() => handleUpdate(index)} className="btn btn-primary btn-sm">
                                    Update
                                </button>
                                <button onClick={() => removeTodo(index)} className="btn btn-danger btn-sm ml-2">
                                    Delete
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};
