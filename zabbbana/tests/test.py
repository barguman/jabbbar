import unittest
from .credentials import *
from zabbbana import Zabbbana

class BaseTest(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.api = Zabbbana(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            scope=['write'],
            state="myrandomkey",
            redirect_uri=REDIRECT_URI
        )

    def test_generate_auth_url(self):
        expected_url = "https://dribbble.com/oauth/authorize?client_id={}&redirect_uri={}&scope={}&state={}"\
                        .format(self.api.client_id, self.api.redirect_uri, self.api.scope, self.api.state)
        auth_url     = self.api.generate_auth_url
        self.assertEqual(auth_url, expected_url)

if __name__ == "__main__":
    unittest.main()
