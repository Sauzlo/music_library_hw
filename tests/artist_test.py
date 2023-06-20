import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("Andrew Bird",1)

    
    def test_artist_has_name(self):
        self.assertEqual("Andrew Bird", self.artist.name)

    def test_artist_has_id(self):
        self.assertEqual(1, self.artist.id)

    def test_artist_change_name(self):
        self.artist.change_name("Dave Bird")
        self.assertEqual("Dave Bird", self.artist.name)