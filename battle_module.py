import utils_module
import pygame
pygame.init()
pygame.mixer.init()

def battle_enemy_village():
    sound = 'BattleFinal.wav'
    sounda = pygame.mixer.Sound(sound)
    sounda.play()
    print("You are in the village ...")
    print("From a backside alley a enemy appears")
    utils_module.random_enemy()