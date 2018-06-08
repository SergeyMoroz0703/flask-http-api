import requests
import unittest
import json


DEFAULT_HEADER = 'application/json'
USER_TO_CREATE_1 = {'name': 'James', 'surname': 'Bond', 'online': False}
USER_TO_CREATE_2 = {'name': 'Alphonse', 'surname': 'Capone', 'online': True}

class TestApiFunctionality(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(TestApiFunctionality, self).__init__(*a, **kw)
        self.host = '127.0.0.1:5000'
        self.db_url = 'users'
        self.url = 'http://{}/{}'.format(self.host, self.db_url)

    def _post_user(self, headers=DEFAULT_HEADER, user_to_create=None):
        _headers = {'content-type': headers}
        _payload = user_to_create
        _response = requests.post(url=self.url, data=json.dumps(_payload), headers=_headers)
        return _response.status_code, _response.json()

    def _get_users_list(self):
        _response = requests.get(url=self.url)
        return _response.status_code, _response.json()

    def _get_user(self, user_to_get=USER_TO_CREATE_1):
        _payload = user_to_get
        _response = requests.get(url=self.url, params=_payload)
        return _response.status_code, _response.json()

    def test_add_user(self):
        status_code, response = self._post_user(user_to_create=USER_TO_CREATE_1)
        self.assertEqual(status_code, 201)
        self.assertTrue(set(USER_TO_CREATE_1.items()).issubset(set(response['result'].items())),
                        msg='User to create is not in {}'.format(response['result']))

    def test_get_users(self):
        status_code_post_1, response_post_1 = self._post_user(user_to_create=USER_TO_CREATE_1)
        status_code_post_2, response_post_2 = self._post_user(user_to_create=USER_TO_CREATE_2)
        users_list = [response_post_1['result'], response_post_2['result']]
        status_code_get_list, response_get_list = self._get_users_list()
        self.assertEqual(status_code_get_list, 200)
        self.assertIn(response_post_1['result'], response_get_list['data'])
        self.assertIn(response_post_2['result'], response_get_list['data'])

    def test_get_one_user(self):
        status_code_post_1, response_post_1 = self._post_user(user_to_create=USER_TO_CREATE_1)
        user_id = response_post_1['result']['id']
        status_code_get_user, response_get_user = self._get_user(user_to_get={'id':user_id})
        self.assertEqual(status_code_get_user, 200)
        # assert just one user with user_id returned
        self.assertEqual(len(response_get_user['data']), 1)
        self.assertIn(response_post_1['result'], response_get_user['data'])



if __name__ == '__main__':
    unittest.main(verbosity=2)