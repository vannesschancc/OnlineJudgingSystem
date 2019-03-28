import React from 'react';
import { shallow } from 'enzyme';

import UsersList from '../UsersList';
import renderer from 'react-test-renderer';

const users = [
    {
        'active': true,
        'email': 'vannesschancc@live.com',
        'id': 1,
        'username': 'vannesschancc'
    },
    {
        'active': true,
        'email': 'chc507@ucsd.edu',
        'id': 2,
        'username': 'chc507'
    } 
];

/*
    In this test, we used the shallow helper method to create the UsersList component and then we retrieved the output and made assertions against it. It's important to note that with "shallow rendering", we can test the component in complete isolation, which helps to ensure child components do not indirectly affect assertions.
*/
test('UsersList renders properly', () => {
    const wrapper = shallow(<UsersList users={users}/>);
    const element = wrapper.find('h4')
    expect(element.length).toBe(2);
    expect(element.get(0).props.children).toBe('vannesschancc');
});

//test ui, make sure that it does not change
test('UserList renders a snapshot properly', () => {
    const tree = renderer.create(<UsersList users={users}/>).toJSON();
    expect(tree).toMatchSnapshot();
});