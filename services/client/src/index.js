import React, { Component } from 'react'; 
import ReactDOM from 'react-dom';
import axios from 'axios';
import UsersList from './components/UsersList';
import AddUser from './components/AddUser';
// class-base components
/*
fd
    1. We created a class-based component, which runs automatically when an instance is created (behind the scenes).
    2. When run, super() calls the constructor of Component, which App extends from.

*/
class App extends Component {
    constructor() {
        super();
        //this.getUsers();
        this.state = {
            users: [],
            username: '',
            email: '', 
        };

        this.addUser = this.addUser.bind(this); 
        this.handleChange = this.handleChange.bind(this)
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

    addUser(event) {
        event.preventDefault();
        console.log('sanity check');
        console.log(this.state);
    
        const data = {
            username: this.state.username, 
            email: this.state.email
        }; 

        axios.post(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`, data)
        .then((res) => {
            this.getUsers(); 
            this.setState({username: '', email:''});
            console.log(res);})
        .catch((err) => {console.log(err);}); 
    }; 

    handleChange(event) {
        const obj = {}; 
        obj[event.target.name] = event.target.value; 
        this.setState(obj);
    }

    render() {
        return (
            <section className="section">
            <div className="container">
                <div className="columns">
                    <div className="column is-half">
                        <br/>
                        <h1 className="title is-1">All Users</h1>
                        <hr/><br/>
                        {/*Adduser is a functional component*/}
                        <AddUser 
                            username={this.state.username}
                            addUser={this.addUser}
                            email={this.state.email}
                            handleChange={this.handleChange}
                        />
                        <br/><br/>
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


