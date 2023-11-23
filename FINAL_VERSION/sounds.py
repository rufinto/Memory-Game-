import pygame

pygame.mixer.init()

sound_button = pygame.mixer.Sound("DATA/SOUNDS/button.mp3")
sound_window = pygame.mixer.Sound("DATA/SOUNDS/window.mp3")
sound_flip = pygame.mixer.Sound("DATA/SOUNDS/flip.mp3")
sound_rightpair = pygame.mixer.Sound("DATA/SOUNDS/right.mp3")
sound_wrongpair = pygame.mixer.Sound("DATA/SOUNDS/wrong.mp3")
sound_good = pygame.mixer.Sound("DATA/SOUNDS/good.mp3")
sound_shuffle = pygame.mixer.Sound("DATA/SOUNDS/shuffle.mp3")


def play_sound(sound) :
    pygame.mixer.Sound.play(sound)

