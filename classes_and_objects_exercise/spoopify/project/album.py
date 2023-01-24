from spoopify.project.song import Song


class Album:
    def __init__(self, name, *song):
        self.name = name
        self.published = False
        self.songs = []
        for el in song:
            self.songs.append(el)

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return f"Cannot add songs. Album is published."

        if song in self.songs:
            return 'Song is already in the album.'

        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name):
        if self.published:
            return "Cannot remove songs. Album is published."

        try:
            song = next(filter(lambda s: s.name == song_name, self.songs))
        except StopIteration:
            return "Song is not in the album."

        self.songs.remove(song)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        return f'Album {self.name}\n' + '\n'.join(f'== {el}' for el in self.songs) + '\n'


