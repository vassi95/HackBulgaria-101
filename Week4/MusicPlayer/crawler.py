from music import Playlist, Song
import os
from datetime import timedelta
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3


class MusicCrawler:

    def __init__(self, path):
        self.path = path
        self.paths = [
            i for i in os.listdir(path) if i.endswith(".mp3")]

    def generate_playlist(self):
        playlist = Playlist(name="Songsss")
        for path in self.paths:
            song = MP3(self.path + path, ID3=EasyID3)
            artist = song["artist"][0]
            album = song["album"][0]
            title = song["title"][0]
            length = str(timedelta(seconds=int(song._length)))
            current = Song(title, artist, album, length)
            current.name = path
            playlist.add_song(current)
        return playlist
