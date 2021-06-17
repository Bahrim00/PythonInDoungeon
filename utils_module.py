import os
import exploring_module
import random
import enemy_module
import player_module
import pygame
pygame.init()
pygame.mixer.init()

def welcome_message():
    welcome = """
    ****************************************************************************************
    *                                   Welcome,stranger.                                  *
    * Here in Hinderlands, You'll get to fight dragons and conquer the deadliest dungeons. *
    *        In a country where magic rules, anything is possible if you wish so.          *
    *                          It all depends on you, brave hero.                          *
    ****************************************************************************************
    """
    print(welcome)



def start_adventure():
    sound = 'Main_Menu.wav'
    sounda = pygame.mixer.Sound(sound)
    sounda.play()

    print('Would you like to start the adventure ? ')
    user_answer = input('Yes or No -> ')

    if user_answer.upper() == 'YES':
        os.system('clear')
        answer = input('''
What type of player are you:
1 for Warrior 2 for Wizzard -->  ''')

        if answer == '1':
            player_name = input('''
You have chosen to be a mighty Warrior
What is your name? ->  ''')
            player = player_module.Warrior(player_name)
            print('Intro to the world')
            input('Press a key to continue... ')
            sounda.stop()
            os.system('clear')
            exploring_module.start_exploring()

        elif answer == '2':
            player_name = input('''
You have chosen to be a mighty Wizard
What is your name? ->''')
            player = player_module.Wizard(player_name)
            print('Intro to the world')
            input('Press a key to continue... ')
            sounda.stop()
            os.system('clear')
            exploring_module.start_exploring()


        else:
            print('Choose a valid option')

    else:
        print('Thank you, Good BYE !')

def random_enemy():
    random_number = random.randint(0, 2)
    if random_number == 0:
        enemy = enemy_module.Goblin()
    elif random_number == 1:
        enemy = enemy_module.Orc()
    elif random_number == 2:
        enemy = enemy_module.Rat()


