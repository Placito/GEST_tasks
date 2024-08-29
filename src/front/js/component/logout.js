import React, { useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { Context } from '../store/appContext';

function LogoutComponent() {
    const navigate = useNavigate();
    const { actions } = useContext(Context);

    const handleLogout = () => {
        console.log("handleLogout is called");
        
        // Assuming `actions.logout` handles token removal and state reset
        actions.logout();  // Trigger the logout action
        
        // Redirect to the login page or home page after logout
        navigate('/login');
    };

    return (
        <div>
            <button className="btn-logout" onClick={handleLogout}>
                Logout
            </button>
        </div>
    );
}

export default LogoutComponent;
