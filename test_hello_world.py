import unittest as ut
from hello_world import app

class FlaskRouteTest(ut.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_greeting_route(self):
        response = self.app.get("/greeting")
        
        self.assertEqual(response.status_code, 200)
        
        # Vérifie que le message attendu est dans la réponse
        self.assertIn(b"Welcome to CI/CD 101 using GitHub Actions!", response.data)

        # Vérifie simplement que <html> est présent quelque part
        self.assertIn(b"<html>", response.data)

if __name__ == "__main__":
    ut.main()
