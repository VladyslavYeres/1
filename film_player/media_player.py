import os
import string

class Player:
    def __init__(self, name, volume=50, quality='medium'):
        self.name = name
        self.volume = volume
        self.quality = quality
        self.playing = False
        self.last_time_played = None

    def play(self):
        if not self.playing:
            print(f'{self.name} is now playing.')
            self.playing = True
        else:
            print(f'{self.name} is already playing.')

    def pause(self):
        if self.playing:
            print(f'{self.name} is now paused.')
            self.playing = False
        else:
            print(f'{self.name} is already paused.')

    def save_last_time(self, time):
        self.last_time_played = time
        print(f'Last time played was saved as {time}.')

    def change_quality(self, quality):
        self.quality = quality
        print(f'Quality changed to {quality}.')

    def set_volume(self, volume):
        self.volume = volume
        print(f'Volume set to {volume}.')

os.mkdir('film_storage')
for letter in string.ascii_uppercase:
    letter_dir = os.path.join('film_storage', letter)
    os.mkdir(letter_dir)