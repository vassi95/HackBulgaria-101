import unittest
from music import Song, Playlist


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")

    def test_init(self):
        self.assertTrue(isinstance(self.song, Song))
        self.assertEqual(self.song._title, "Odin")
        self.assertEqual(self.song._artist, "Manowar")
        self.assertEqual(self.song._album, "The Sons of Odin")
        self.assertEqual(self.song._length, "3:44")

    def test_str(self):
        result = "Manowar - Odin from The Sons of Odin - 3:44"
        self.assertEqual(str(self.song), result)

    def test_eq(self):
        song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        self.assertTrue(song1 == self.song)

    def test_length_of_song(self):
        self.assertEqual(self.song.length_of_song(seconds=True), 224)
        self.assertEqual(self.song.length_of_song(minutes=True), 3)


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        self.playlist = Playlist(name="Code", repeat=True, shuffle=True)

    def test_init(self):
        self.assertTrue(isinstance(self.playlist, Playlist))
        self.assertEqual(self.playlist.name, "Code")
        self.assertEqual(self.playlist.repeat, True)
        self.assertEqual(self.playlist.shuffle, True)

    def test_add_song(self):
        self.playlist.add_song(self.song)
        self.assertTrue(self.song in self.playlist.songs)

    def test_remove_song(self):
        self.playlist.songs = [self.song]
        self.playlist.remove_song(self.song)
        self.assertEqual(self.playlist.songs, [])

    def test_add_songs(self):
        song1 = Song("Always", "Bon Jovi", "Best of", "4:35")
        song2 = Song("Till  collapseI", "Eminem", "The Eminem show", "3:40")
        self.playlist.add_songs([song1, song2])
        self.assertTrue(song1 in self.playlist.songs)
        self.assertTrue(song2 in self.playlist.songs)

    def test_total_length(self):
        song1 = Song("Always", "Bon Jovi", "Best of", "4:35")
        song2 = Song("Till  collapseI", "Eminem", "The Eminem show", "3:40")
        self.playlist.songs = [song1, song2]
        self.assertEqual(self.playlist.total_length(), "00:08:15")

    def test_artists(self):
        song1 = Song("Always", "Bon Jovi", "Best of", "4:35")
        song2 = Song("Till  collapseI", "Eminem", "The Eminem show", "3:40")
        self.playlist.add_songs([song1, song2])
        length = self.playlist.total_length()
        self.assertEqual(self.playlist.total_length(), length)

    def test_next_song(self):
        song1 = Song("Always", "Bon Jovi", "Best of", "4:35")
        song2 = Song("Till  collapseI", "Eminem", "The Eminem show", "3:40")
        self.playlist.songs = [song1, song2]
        self.assertEqual(self.playlist.next_song(), song1)
        self.assertEqual(self.playlist.next_song(), song2)



if __name__ == '__main__':
    unittest.main()
