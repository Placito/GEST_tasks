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
			]
		},
		actions: {
			// Use getActions to call a function within a fuction
			exampleFunction: () => {
				getActions().changeColor(0, "green");
			},

			getMessage: async () => {
				try{
					// fetching data from the backend
					const resp = await fetch(process.env.BACKEND_URL + "/api/hello")
					const data = await resp.json()
					setStore({ message: data.message })
					// don't forget to return something, that is how the async resolves
					return data;
				}catch(error){
					console.log("Error loading message from backend", error)
				}
			},
			login: (username, password) => {
				const opts = {
					method: 'POST',
					headers: {
						"content-Type": "application/json"
					},
					body: JSON.stringify({
						"username": username,
						"passsword": password
					})
				}
				fetch('https://glorious-space-succotash-7jxpv6jj6xw2pp6j-3001.app.github.dev/api/token', opts)
				.then(resp => {
					console.log(resp)
					if(resp.status === 200) return resp.json();
					else alert("There has been some error");
				})
				.then(data => {
					sessionStorage.setItem("token", data.access_token);
				})
				.catch(error => {
					console.error(error);
				})
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
			}

		}
	};
};

export default getState;
