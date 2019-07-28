import unittest
from app import app


# file name must start with 'test_'
class TestUserMethod(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()

    def test_get(self):
        response = self.app.post('/model/predict', data={
            'instances': [1, 2, 3]
        })
        self.assertEqual(response.json, {
            'predictions': [2.5, 3, 3.5]
        })


if __name__ == '__main__':
    unittest.main()
