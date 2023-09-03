import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Barrowlands")
        self.room2 = Room("Hive")
        self.room3 = Room("Unicorn")
        self.room4 = Room("Dusk")

        self.guest = Guest("Ryan")
        self.guest2 = Guest("Olly")

        self.song = Song("Don't Stop Me Now", "Queen")
        self.song2 = Song("Mr. Brightside", "The Killers")
        self.song3 = Song("Rasputin", "Boney M")
        self.song4 = Song("September", "Earth, Wind, and Fire")

    # def test_guest_has_name(self) --> do this!!


    def test_add_guest_to_room(self):
        self.room.add_guest_to_room(self.guest)
        self.assertEqual([self.guest], self.room.singers) #[self.gues](name) is now added to self.room.singerds

    def test_kick_guest_from_room(self):
        self.room.add_guest_to_room(self.guest)
        self.room.kick_guest_from_room(self.guest)
        self.assertEqual(0, len(self.room.singers)) #would it show nothing, would it show [], or would it show "Cam"

    def add_songs_to_room(self):
        self.room.add_songs_to_room(self.song)
        self.assertEqual([self.song], self.room.songs)