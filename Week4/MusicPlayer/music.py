from json import dumps
from json import loads
import random
import tabulate


class Song:
    def __init__(self, title, artist, album, length):
        self._title = title
        self._artist = artist
        self._album = album
        self._length = length

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.length)

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash(self.__str__())

    def length_of_song(self, seconds=False, minutes=False, hours=False):
        part = self.length.split(':')
        length1 = len(part)
        if length1 == 2:
            part = ["0"] + part
        if seconds is True:
            return int(part[0]) * 3600 + int(part[1]) * 60 + int(part[2])
        elif minutes is True:
            return int(part[0]) * 60 + int(part[1])
        elif hours is True:
            return int(part[0])
        else:
            return self.length


class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songs = []
        self.current_song = 0
        self.played = set()

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        if not isinstance(song, Song):
            raise ValueError
        if song not in self.songs:
            raise ValueError("the song isn't in the playlist")
        self.songs.remove(song)

    def add_songs(self, songs):
        for s in songs:
            self.add_song(s)

    def total_length(self):
        total_len = 0
        for song in self.songs:
            total_len += song.length(seconds=True)
        hours = total_len // 3600
        total_len -= hours
        minutes = total_len // 60
        total_len -= minutes
        seconds = total_len // 60
        total_len = "{}:{}:{}".format(hours, minutes, seconds)
        return total_len

    def artists(self):
        artistss = {}
        for song in self.songs:
            if song.artist in artistss:
                artistss[song.artist] += 1
            else:
                artistss[song.artist] = 1
        return artistss

    def shuffle(self):
        random_song = random.choice(self.songs)
        while random_song in self.played:
            random_song = random.choice(self.songs)
        self.played.add(random_song)
        if len(self.songs) == len(self.played):
            self.played = set()
        return random_song

    def next_song(self):
        if self.shuffle is True:
            return self.shuffle()
        if not self.current_song < len(self.songs) and self.repeat is True:
            self.current_song = 0
        song = self.songs[self.current_song]
        self.current_song += 1
        return song
        if self.current_song < len(self.songs) and self.repeat is False:
            song = self.songs[self.current_song]
            self.current_song += 1
            return song
        else:
            print("You reached end of playlist!")

    def pprint_playlist(self):
        table = []
        for song in self.songs:
            table += [[song._artist, song._title, song._length]]
        print(tabulate.tabulate(table, headers=['Artist', 'Song', 'Length']))

    def prepare_json(self):
        songs = [song.__dict__ for song in self.songs]
        data = {"name": self.name,
                "songs": songs}
        return data

    def save(self):
        filee = self.name.replace(" ", "-") + ".json"
        with open(filee, "w") as f:
            f.write(dumps(self.prepare_json()))

    @staticmethod
    def load(filename):
        with open(filename, "r") as f:
            contents = f.read()
            info = loads(contents)
            a = Playlist(info["songs"], shuffle=False, repeat=True)
            for dict_song in info["songs"]:
                song = Song(artist=dict_song["artist"], title=dict_song["title"], album=dict_song["album"], length=dict_song["length"])
                a.add_songs(song)
            return a


def main():
    songs = []
    songs.append(Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44"))
    songs.append(Song(title="The Sons of Odin", artist="Manowar", album="album title goes here", length="3:14"))
    a = Playlist(name="Code", repeat=True, shuffle=True)
    a.add_songs(songs)
    a.pprint_playlist()
    a.save()
    a.load("Code.json")
if __name__ == '__main__':
    main()
