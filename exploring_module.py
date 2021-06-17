import os
import battle_module
import pygame
pygame.init()
pygame.mixer.init()

def start_exploring():
    sound = 'Exploring.wav'
    sounda = pygame.mixer.Sound(sound)
    sounda.play()
    print('''
You are in the middle of a crossroads
You have 3 path in front of you:
   1 - Going to a village
   2 - Going to a forest
   3 - Going to a desert''')
    path_option = input('What is your desteny? ')
    if (path_option == '1'):
        os.system("clear")
        print("Going in the village ...")
        input("Press enter to continue ...")
        battle_module.battle_enemy_village()

    elif (path_option == '2'):
        os.system("clear")
        print("Going in the Dark and Misty Forest ...")
        input("Press enter to continue ...")
    elif (path_option == '3'):
        os.system("clear")
        print("Going in the Desert ...")
        input("Press enter to continue ...")
    else:
        print('Answer not avabile')

