import requests
import unittest
import json


DEFAULT_HEADER = 'application/json'
USER_TO_CREATE = {'name': 'James', 'surname': 'Bond', 'online': False}


class TestApiFunctionality(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(TestApiFunctionality, self).__init__(*a, **kw)
        self.host = '127.0.0.1:5000'
        self.db_url = 'users'
        self.url = 'http://{}/{}'.format(self.host, self.db_url)

    def _post_user(self, headers=DEFAULT_HEADER, user_to_create=USER_TO_CREATE):
        _headers = {'content-type': headers}
        _payload = user_to_create
        _response = requests.post(url=self.url, data=json.dumps(_payload), headers=_headers)
        return _response.status_code, _response.json()

    def _get_users_list(self):
        _response = requests.get(url=self.url)
        return _response.status_code, _response.json()

    def _get_user(self):
        _payload = USER_TO_CREATE
        _response = requests.get(url=self.url, params=_payload)
        return _response.status_code, _response.json()


    def test_add_user(self):
        status_code, response = self._post_user()
        self.assertEqual(status_code, 201)
        self.assertTrue(set(USER_TO_CREATE.items()).issubset(set(response['result'].items())),
                        msg='User to create is not in {}'.format(response['result']))


if __name__ == '__main__':
    unittest.main(verbosity=2)