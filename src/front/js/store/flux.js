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
