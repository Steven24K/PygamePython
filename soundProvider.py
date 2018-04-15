import pygame

class SoundProvider:
    def __init__(self, music_file):
        self.File = music_file
        self.Music = pygame.mixer_music.load(self.File)
    def Play(self, loops):
        pygame.mixer_music.play(loops, 0)
