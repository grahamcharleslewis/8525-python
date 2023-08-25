import unittest

def hello(name):
    return "Hello " + name

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello("Fred"), "Hello Fred")
        
    def test_hello_empty_string(self):
        self.assertEqual(hello(""), "Hello ")

    def test_hello_space(self):
        self.assertEqual(hello(" "), "Hello  ")

