import unittest
from pagina import app
class TestHello(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.data, b'Hello Practica 1 de Software Avanzado xd!')
if __name__ == '__main__':
    unittest.main()