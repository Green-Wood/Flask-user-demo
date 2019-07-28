import unittest
from flask import json
from app import app


# file name must start with 'test_'
class TestUserMethod(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()

    def test_model(self):
        response = self.app.post(
            '/api/model/predict',
            json={
                'instances': [1, 2, 3]
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            'predictions': [2.5, 3, 3.5]
        })


if __name__ == '__main__':
    unittest.main()
