import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Don't Stop Me Now", "Queen")
        self.song2 = Song("Mr. Brightside", "The Killers")
        self.song3 = Song("Rasputin", "Boney M")
        self.song4 = Song("September", "Earth, Wind, and Fire")
        