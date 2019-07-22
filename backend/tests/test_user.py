import unittest
from app import app


# file name must start with 'test_'
class TestUserMethod(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()
        self.app.post('/security/register', data={
            'username': 'greenwood',
            'password': '123'
        })

    def test_get(self):
        response = self.app.get('/user/1')
        self.assertEqual(response.json, {
            'id': 1,
            'username': 'greenwood'
        })


if __name__ == '__main__':
    unittest.main()
