import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Ryan")
        self.guest2 = Guest("Olly")
        self.guest3 = Guest("Cam")
        self.guest4 = Guest("Sophia")
