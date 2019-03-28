import React from 'react';

/*
Notice how we used props instead of state in this component. Essentially, you can pass state to a component with either props or state:
    Props: data flows down via props (from state to props), read only
    State: data is tied to a component, read and write

*/
const UserList = (probs) => {
    return (
        <div>
            {
                probs.users.map((user) => {
                    return (
                        <h4
                            key={user.id}
                            className='box title is-4'
                        >{ user.username} 
                        </h4>
                    )
                })
            }
        </div>
    )
};

export default UserList;