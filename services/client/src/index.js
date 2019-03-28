import React, { Component } from 'react'; 
import ReactDOM from 'react-dom';
import axios from 'axios';
import UsersList from './components/UsersList';
// class-base components
/*

    1. We created a class-based component, which runs automatically when an instance is created (behind the scenes).
    2. When run, super() calls the constructor of Component, which App extends from.

*/
class App extends Component {
    constructor() {
        super();
        //this.getUsers();
        this.state = {
            users: []
        };
    };
    
    componentDidMount() {
        this.getUsers();
    };
    
    /*
        Add a state to user 
    */

    getUsers() {
        axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
        .then((res) => {this.setState({users: res.data.data.users}); })
        .catch((err) => {console.log(err);});
    };
    render() {
        return (
            <section className="section">
                <div className="container">
                    <div className="columns">
                        <div className="columns is-one-third">
                        <br/>
                        <h1 className="title is-1">All Users</h1>
                        <hr/><br/>
                        {/* new */}
                        <UsersList users={this.state.users}/>
                        </div>
                    </div>
                </div>
            </section>
        )
    }
};

ReactDOM.render(
    <App />,
    document.getElementById('root')
);


