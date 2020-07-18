import unittest
import os
from app import app
from models import db, Movie, Actor

database_path = os.environ['DATABASE_URL']
assistant_token = os.getenv('ASSISTANT_TOKEN')
director_token = os.getenv('DIRECTOR_TOKEN')
producer_token = os.getenv('PRODUCER_TOKEN')


def set_auth_header(role):
    if role == 'assistant':
        return {'Authorization': 'Bearer {}'.format(assistant_token)}
    elif role == 'director':
        return {'Authorization': 'Bearer {}'.format(director_token)}
    elif role == 'producer':
        return {'Authorization': 'Bearer {}'.format(producer_token)}


class MainTestCase(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        #app.config['TESTING'] = True
        # app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        # app.config['SQLALCHEMY_DATABASE_URI'] = database_path
        self.app = app
        self.client = self.app.test_client
        # self.app = app.test_client()
        db.drop_all()
        db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass
    
    # Test of Actor endpoints
    
    
    def test_add_actor_fail(self):
        res = self.client().post(
            '/actors', json={}, headers=set_auth_header('producer'))
        self.assertEqual(res.status_code, 400)
        print(res.get_json())
        self.assertEqual(res.get_json()['success'], False)

    def test_add_actor_unauthorized(self):
        data = {
            "name": "name",
            "gender": "M"
        }
        res = self.client().post('/actors', json=data, headers=set_auth_header('assistant'))
        print(res.get_json())
        self.assertEqual(res.status_code, 403)


    def test_add_actor(self):
        data = {
            "name": "urmmi",
            "gender": "M"
        }
        res = self.client().post('/actors', json=data, headers=set_auth_header('producer'))
        self.assertEqual(res.status_code, 201)
        print('add')
        print(res.get_json())
        self.assertEqual(res.get_json()['success'], True)

    def test_get_actors_unauthorized(self):
        res = self.client().get(
            '/actors', headers=set_auth_header(''))
        self.assertEqual(res.status_code, 401)

    def test_get_actors(self):
        res = self.client().get(
            '/actors', headers=set_auth_header('assistant'))
        print('get')
        print(res.get_json())
        self.assertEqual(res.status_code, 200)


    # def test_edit_actor_unauthorized(self):
    #     data = {
    #         "name": "Alamin",
    #         "gender": "M"
    #     }

    #     res = self.client().patch('/actors/1', json=data,
    #                               headers=set_auth_header('assistant'))
    #     self.assertEqual(res.status_code, 403)
    #     # self.assertEqual(res.get_json()['message'], 'unauthorized')

    # def test_edit_actor_fail(self):
    #     data = {
    #         "name": "Sandy",
    #         "gender": "F"
    #     }
    #     res = self.client().patch('/actors/303', json=data,  headers=set_auth_header('producer'))
    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(res.get_json()['message'], 'not found')

    def test_edit_actor(self):
        data = {
            "name": "Alamin",
            "gender": "M"
        }
        res = self.client().patch('/actors/1', json=data, headers=set_auth_header('producer'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()['success'], True)


    # def test_delete_actor_unauthorized(self):
    #     res = self.client().delete('/actors/1', headers=set_auth_header('assistant'))
    #     self.assertEqual(res.status_code, 403)

    # def test_delete_actor_fail(self):
    #     res = self.client().delete('/actors/101', headers=set_auth_header('producer'))
    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(res.get_json()['success'], False)

    # def test_delete_actor(self):
    #     res = self.client().delete(
    #         '/actors/1', headers=set_auth_header('producer'))
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(res.get_json()['success'], True)


    
if __name__ == '__main__':
    unittest.main()
