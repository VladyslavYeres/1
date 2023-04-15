class Film:
    def __init__(self, title, genre, director, duration, release_year, storage_address):
        self.title = title
        self.genre = genre
        self.director = director
        self.duration = duration
        self.release_year = release_year
        self.is_watched = False
        self.storage_address = storage_address

    def play(self):
        print(f'Now playing: {self.title}')

    def pause(self):
        print(f'Paused: {self.title}')

    def mark_as_watched(self):
        self.is_watched = True
        print(f'{self.title} marked as watched.')

    def get_info(self):
        return f'Title: {self.title}\n' \
               f'Genre: {self.genre}\n' \
               f'Director: {self.director}\n' \
               f'Duration: {self.duration} min\n' \
               f'Release Year: {self.release_year}\n' \
               f'Watched: {"Yes" if self.is_watched else "No"}'
    def upload_file(self):
        open(f"film_storage/{self.title[0]}/{self.title}.txt", "w")

    def get_film_address(self):
        print(f"film_storage/{self.title[0]}/{self.title}.txt")
