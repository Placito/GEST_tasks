import axios from 'axios';
import { json } from 'react-router-dom';

const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			message: null,
			demo: [
				{
					title: "FIRST",
					background: "white",
					initial: "white"
				},
				{
					title: "SECOND",
					background: "white",
					initial: "white"
				}
			],
			token: [],
			users: []
		},
		actions: {
			// Use getActions to call a function within a fuction
			exampleFunction: () => {
				getActions().changeColor(0, "green");
			},
			  logout: () => {
				axios.post('/logout')
					.then(response => {
						if (response.data.success === 'true') {
							console.log("Logout successful");
						} else {
							console.error('Logout failed:', response.data.msg);
						}
					})
				localStorage.removeItem('access_token'); // Always remove token

			},
			getUsers: () => {
				fetch('https://randomuser.me/api/', {
						method: 'get',
						headers: {
							'Content-Type': 'application/json'
						}
					})
					.then(res => {
						console.log(res)
						return res.json()
					})
					.then(data => 
						setStore({ users: data.results })
						)
					.catch(error => console.log(error))
			},
			//function to add a new contact
			addUser: async (username, name, role, password) => {
				const opts = {
					method: "POST",
					headers: {
						"Content-Type": "application/json",
					},
					body: JSON.stringify({
						username: username,
						name: name,
						role: role,
						password: password,
					}),
				};
				try {
					const resp = await fetch(
						`${process.env.BACKEND_URL}/create-user`,
						opts
					);
					const data = await resp.json();

					if (resp.status === 201) {
						console.log("User created successfully", data);
						setStore({ users: data })
						return true;
					} else {
						alert(`Error: ${data.message}`);
					}
				} catch (error) {
					console.error("An error occurred while signing up", error);
				}
				return false;
			},
			//function that allows to update users
			update: (index, updatedTask) => {
                const store = getStore();
                const tasks = [...store.tasks];
                
                // Update the specific task at the given index
                tasks[index] = updatedTask;

                // Update the global state with the modified tasks array
                setStore({ tasks: tasks });

                // Optional: If you're working with an API, you can also send the update request
                fetch(`https://jsonplaceholder.typicode.com/todos/${index}`, {
                    method: 'PUT', // or 'PATCH' depending on your API
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ title: updatedTask })
                })
                .then(response => response.json())
                .then(data => console.log('Update Success:', data))
                .catch(error => console.error('Update Error:', error));
            }
        },
			changeColor: (index, color) => {
				//get the store
				const store = getStore();

				//we have to loop the entire demo array to look for the respective index
				//and change its color
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});

				//reset the global store
				setStore({ demo: demo });
			},
		}
	};


export default getState;
