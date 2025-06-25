class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}    # Ensure this is a persistent class variable
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1
        Song.genres.append(genre)
        Song.artists.append(artist)

        # Update genre_count as songs are created
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # Update artist_count as songs are created
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

    @classmethod
    def add_to_genres(cls):
        return list(set(cls.genres))

    @classmethod
    def add_to_artists(cls):
        return list(set(cls.artists))

    @classmethod
    def add_to_genre_count(cls):
        return cls.genre_count

    @classmethod
    def add_to_artist_count(cls):
        return cls.artist_count
