import requests
import unittest

DEFAULT_HEADER = 'application/json'
USER_TO_CREATE = {'name': 'James', 'surname': 'Bond', 'online': False}



class TestApiFunctionality(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(TestApiFunctionality, self).__init__(*a, **kw)
        self.host = '127.0.0.1:5000'
        self.db_url = 'users'
        self.url = 'http://{}/{}'.format(self.host, self.db_url)

    def post_user(self):
