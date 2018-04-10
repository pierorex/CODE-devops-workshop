from unittest import TestCase
from ..base import TestClient
from calculator.app import app


class ViewTests(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = TestClient(app)

    def test_multiply(self):
        response = self.client.get('calc/3*10')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.body, '30')
        pass

    def test_invalid_http_request(self):
        response = self.client.get('/calc/10/10000')
        self.assertEqual(response.status_code, '403')
