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
			login: async (username, password) => {
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
				console.log(opts)
				try {
					const resp = await fetch('https://glorious-space-succotash-7jxpv6jj6xw2pp6j-3001.app.github.dev/api/token', opts)
					if(resp.status !== 200) {
						console.log(resp)
						alert("There has been some error");
						return false;
				}
					const data = await resp.jon();
					console.log("This came from the backend", data);
					sessionStorage.setItem("token", data.access_token);
					setStore({token: data.access_token})
					return true;
				}
				catch(error){
					console.error("There has been an error!");
				}
				
			},
			logout: () => {
				sessionStorage.removeItem("token");
				setStore({token: null});
			},
			getUsers: () => {
				fetch('https://randomuser.me/api', {
						method: 'Post',
						headers: {
							'Content-Type': 'application/json'
						},
						body: JSON.stringify({
							name: 'User 1'
						})
					})
					.then(res => {
						return res.json()
					})
					.then(data => 
						console.log(data),
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
			}

		}
	};
};

export default getState;
