# Importamos nosso app
from app import meu_web_app

# Importamos a biblioteca de testes
import unittest


class TestHomeView(unittest.TestCase):

    def setUp(self):
        app = meu_web_app.test_client()
        self.response = app.get('/')

    # Testamos se a resposta e 200 ("ok")
    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    # Testamos se a nossa home retorna a string "ok"
    def test_html_string_response(self):
        self.assertEqual("ok", self.response.data.decode('utf-8'))

    # Testamos se o content_type da resposta da home esta correto
    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)
