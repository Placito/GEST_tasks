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
			token: null,
			users: [],
		},
		actions: {
			// Use getActions to call a function within a fuction
			exampleFunction: () => {
				getActions().changeColor(0, "green");
			},

			syncTokenFromSessionStorage: () => {
				const token = sessionStorage.getItem("token");
				if (token && token != "" && token != undefined) setStore({token: token});
			},
			/*login: async function login(username, password) {
				let flag = true;
				if (username === "") {
				  flag = false;
				  setEmailFlag(true);
				}
				if (password === "") {
				  flag = false;
				  setPasswordFlag(true);
				}
				if (!flag) {
				  setMessage("Wrong credential");
				  return;
				}
				const payload = {
				  username: username,
				  password: password,
				};
				try {
				  const response = await axios.post(process.env.BACKEND_URL + "/api/token", payload);
				  console.log(response);
			
				  if (response.data.success === "true") {
					// Store access token in local storage
					localStorage.setItem('access_token', response.data.access_token);
					//console.log("Login successful");
					console.log("Stored Token: ", localStorage.getItem('access_token'));
					//console.log(localStorage.getItem('access_token'));
			
					console.log("Navigating to profile"); // to check if Navigation function is called
			
					if (localStorage.getItem('access_token')) {
					  setIsLoggedIn(true);
					  navigate("/profile");
			
					} else {
					  console.log("Token not set");
					}
				  } else {
					setAPIFlag(true);
					setMessage(response.data.msg);
					console.log("Login failed");
				  }
				} catch (error) {
				  if (error.response) {
					console.log(error.response);
				  }
				}
			  },*/
			logout: () => {
				sessionStorage.removeItem("token");
				setStore({token: null});
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
