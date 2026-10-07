import unittest
from app import greet, add_numbers, is_service_healthy

class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertIn("Hello, Alice!", greet("Alice"))

    def test_add_numbers(self):
        self.assertEqual(add_numbers(10, 20), 30)

    def test_health(self):
        self.assertTrue(is_service_healthy())

if __name__ == "__main__":
    unittest.main()
