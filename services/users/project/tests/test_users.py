# services/users/project/tests/test_users.py

import json 
import unittest

from project.tests.base import BaseTestCase
from project import db 
from project.api.models import User 
from project.tests.utils import add_user 

class TestUserService(BaseTestCase):
    '''Test for the User Servie '''
    def test_user(self):
        ''' Ensure the /ping route behaves correctly.'''
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])
    
    
    def test_add_user(self):
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'vannesschancc',
                    'email': 'vannesschancc@live.com',
                    'password': 'greaterthaneight'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('vannesschancc@live.com was added!', data['message'])
            self.assertIn('success', data['status'])

    def test_add_user_invalid_json(self):
        """Ensure error is thrown if the JSON object is empty."""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload', data['message'])
            self.assertIn('fail', data['status'])           

    def test_add_user_invalid_json_keys(self):
        """
        Ensure error is thrown if the JSON object does not have a username key.
        """
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'email': 'vannesschancc@live.com', 
                    'password': 'greaterthaneight'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_user_invalid_json_keys_no_password(self):
        """
        Ensure error is thrown if the JSON object
        does not have a password key.
        """
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(dict(
                    username='michael',
                    email='michael@reallynotreal.com')),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])


    def test_add_user_duplicate_email(self):
        """Ensure error is thrown if the email already exists."""
        with self.client:
            self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'vannesschancc',
                    'email': 'vannesschancc@live.com',
                    'password': 'greaterthaneight'
                }),
                content_type='application/json',
            )
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'vannesschancc',
                    'email': 'vannesschancc@live.com', 
                    'password': 'greaterthaneight'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn(
                'Sorry. That email already exists.', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_user(self):
        """Ensure single user behaves correctly"""
        user = add_user('vannesschancc', 'vannesschancc@live.com','greaterthaneight')

        with self.client:
            response = self.client.get(f'/users/{user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('vannesschancc', data['data']['username'])
            self.assertIn('vannesschancc@live.com', data['data']['email'])
            self.assertIn('success', data['status'])
    
    def test_all_users(self):
        """Ensure get all users behaves correctly."""
        add_user('vannesschancc', 'vannesschancc@live.com', 'greaterthaneight')
        add_user('cchen', 'cchen@unomaha.edu', 'greaterthaneight')

        with self.client:
            response = self.client.get('/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['users']), 2)
            self.assertIn('vannesschancc', data['data']['users'][0]['username'])
            self.assertIn('vannesschancc@live.com', data['data']['users'][0]['email'])
            self.assertIn('cchen', data['data']['users'][1]['username'])
            self.assertIn('cchen@unomaha.edu', data['data']['users'][1]['email'])
            self.assertIn('success', data['status'])

    def test_main_no_user(self):
        """Ensure the main route behaves correctly when no users have been added to the database."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'All Users', response.data)
        self.assertIn(b'<p>No users!</p>', response.data)

    def test_main_with_user(self):
        """Ensure the main route behaves correctly when users have been added to the database."""
        add_user('vannesschancc', 'vannesschancc@live.com', 'greaterthaneight')
        add_user('chc507', 'chc507@ucsd.edu', 'greaterthaneight')
        with self.client:
            response=self.client.get('/')
            self.assertEqual(response.status_code,200)
            self.assertIn(b'All Users', response.data)
            self.assertNotIn(b'<p>No users!</p>', response.data)
            self.assertIn(b'vannesschancc', response.data)
            self.assertIn(b'chc507', response.data)

    def test_main_add_user(self):
        """
        Ensure a new user can be added to the database via a POST request.
        """
        with self.client:
            response = self.client.post(
                '/',
                data=dict(username='michael', email='michael@sonotreal.com', password='greaterthaneight'),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'All Users', response.data)
            self.assertNotIn(b'<p>No users!</p>', response.data)
            self.assertIn(b'michael', response.data)


if __name__ == '__main__':
    unittest.main()