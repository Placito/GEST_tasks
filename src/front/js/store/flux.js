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
			users: [],
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
			getUsersById: (id, setCharacter) => {
				fetch(`https://randomuser.me/api/${id}`)
				.then(res => {
					if (!res.ok) throw Error(res.statusText);
					return res.json();
				})
				.then(response => {
					setCharacter(response.result);
				})
				.catch(error => console.error(error));
			},
			//function to add a new contact
			addUser: (newUser) => {
				//get the store
				const store = getStore();
				const newUser = store.users.concat(newUser);
			
				//a fetch to update the user with the new user
				fetch('https://randomuser.me/api/', {
					method: 'POST',
					body: JSON.stringify(newUser),
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

				//reset the global store
				setStore({ users: newUser });
			},
			//function that allows to update users
			update: (index, user) => {
				const store = getStore();
			console.log(index, user)
				const contact = store.users.map((c, i) => {
					if (index == i) {
						c = user
					}
					return c
				});

			console.log("test", user)
				setStore({ users: user });
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
};

export default getState;
