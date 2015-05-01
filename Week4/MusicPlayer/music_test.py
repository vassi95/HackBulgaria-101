import unittest
from music import Song


class TestSong(unittest.TestCase):

    def test_init(self):
        self.my_song = Song("Always", "Bon Jovi", "best of", "3:45")
        self.assertEqual(self.my_song._title, "Always")
        self.assertEqual(self.my_song._artist, "Bon Jovi")
        self.assertEqual(self.my_song._album, "best of")
        self.assertEqual(self.my_song._length, "3:45")

    def test_str(self):
        self.my_song = Song("Always", "Bon Jovi", "best of", "3:45")
        self.assertEqual(str(self.my_song), "Always - Bon Jovi from best of - 3:45")

    def test_eq(self):
        self.my_song = Song("Always", "Bon Jovi", "best of", "3:45")
        self.other_song = Song("Bed of roses", "Bon Jovi", "best of", "4:00")
        self.assertEquals("Always - Bon Jovi from best of - 3:45", "Bed of roses - Bon Jovi from best of - 4:00")

if __name__ == '__main__':
    unittest.main()
