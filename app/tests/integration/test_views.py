from unittest import TestCase
from ..base import TestClient
from app import app


class ViewTests(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = TestClient(app)

    def test_multiply(self):
        response = self.client.get('calc/3*10')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.body, b'30')

    def test_division_by_zero(self):
        response = self.client.get('/calc/10/0')
        self.assertEqual(response.status_code, 403)

    def test_too_high_number(self):
        response = self.client.get('/calc/10/10000')
        self.assertEqual(response.status_code, 403)

    def test_too_low_number(self):
        response = self.client.get('/calc/-10000*10')
        self.assertEqual(response.status_code, 403)

    def test_nan(self):
        response = self.client.get('/calc/this-is-nan')
        self.assertEqual(response.status_code, 404)
