import Enemy
import random
import os
import Player
import pygame
pygame.init()
pygame.mixer.init()


introMsg = '''
*************************************************
*                                               *
*             Welcome,stranger.                 *
*                                               *
*  Here in Hinderlands, you'll get to fight     *
*  dragons and conquer the deadliest dungeons.  *
*  In a country where magic rules, anything     *
*       is possible if you wish so.             *
*    It all depends on you, brave hero.         *
*                                               *
*************************************************
'''

sound = 'Main_Menu.wav'
sounda = pygame.mixer.Sound(sound)
sounda.play()
print(introMsg)
print('Would you like to start the adventure ? ')
user_answer = input('Yes or No -> ')

if user_answer.upper() == 'YES':
    print('OK')
    os.system('clear')
    answer = input('''
What type of player are you:
1 for Warrior 2 for Wizzard -->  ''' )
    if answer == '1':
        player_name = input('''
You have chosen to be a mighty Warrior
What is your name? ->
        ''')
        player = Player.Warrior(player_name)
        print('Intro to the world')
        input('Press a key to continue... ')

        os.system('clear')
        sound = 'Exploring.wav'
        sounda = sounda.stop()
        sounda = pygame.mixer.Sound(sound)
        sounda.play()
        print('''You are in the middle of a crossroads
You have 3 path in front of you:
1 - Going to a village
2 - Going to a forest
3 - Going to a desert
''')
        path_option = input('What is your desteny? ')

        #Comment:
        '''Create a methood ath(userPath)
         That uses the returnet value from crossroads'''


        if(path_option == '1'):
         # in_the_village() from utils
            print('you are in the village...')
            print('From a backside ally a enemy appears')
            random_number = random.randint(0,2)
            sound = 'BattleFinal.wav'
            sounda = sounda.stop()
            sounda = pygame.mixer.Sound(sound)
            sounda.play()
            if random_number == 0:
                enemy = Enemy.Goblin()
                input('Press a key to continue')
            elif random_number == 1:
                enemy = Enemy.Orc()
                input('Press a key to continue')
            elif random_number == 2:
                enemy = Enemy.Rat()
                input('Press a key to continue')
            else:
                print('Invalid enemy')
        elif(path_option =='2'):
    # in_the_forest() from utils
            print('You are in the forest...')
        elif(path_option =='3'):
    # in_the_desert from utils
            print('You are in the desert...')
        else:
            print('Answer not avabile')






    elif answer == '2':
        player_name = input('''
You have chosen to be a mighty Wizard
What is your name? ->
        ''')
        player = Player.Wizard(player_name)
        print('Intro to the world')
        os.system('clear')


    else:
        print('Choose a valid option')

else:
    print('Thank you, Good BYE !')

