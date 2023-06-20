import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):

    def setUp(self):
        self.album = Album("My Finest Work Yet", "Indie", "Andrew Bird", 1)

    
    def test_album_has_title(self):
        self.assertEqual("My Finest Work Yet", self.album.title)

    def test_album_has_genre(self):
        self.assertEqual("Indie", self.album.genre)

    def test_album_has_artist(self):
        self.assertEqual("Andrew Bird", self.album.artist)

    def test_album_has_id(self):
        self.assertEqual(1, self.album.id)

    def test_album_change_title(self):
        self.album.change_title("Are We Not Burning")
        self.assertEqual("Are We Not Burning", self.album.title)