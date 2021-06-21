import random
import os
import enemy
import pygame
pygame.init()
pygame.mixer.init()
import battle


class Utils:  # creem o CLASA UTILS pentru a stoca multiple functii utile
    @staticmethod  # creem o metoda statica cu functia INTRO
    def intro():
        sound = 'Main_Menu.wav'    #
        sounda = pygame.mixer.Sound(sound)
        sounda.play()

        intro_msg = '''
    ****************************************************************************************
    *                                   Welcome,stranger.                                  *
    * Here in Hinderlands, You'll get to fight dragons and conquer the deadliest dungeons. *
    *        In a country where magic rules, anything is possible if you wish so.          *
    *                          It all depends on you, brave hero.                          *
    **************************************************************************************** '''
        print(intro_msg)

        return

    @staticmethod
    def start_game():
        try:
            start = input('You are ready for ADVENTURE? ( Y/N )')
            start_game = False
            if start.upper() == 'Y':
                start_game = True
            elif start.upper() == 'N':
                start_game = False
            else:
                print('Please choose between Y or N ')

            while start_game:
                if start.upper() == 'Y':
                    os.system('clear')
                    index = 1
                    characters = ('Warrior', 'Wizzard', 'Archer')

                    print('These are the strongest beings ')
                    for character in characters:
                        print(f'{index} - {character}')
                        index += 1
                    user_character = int(input('Please choose your character (1,2,3): '))

                    if user_character == 1:
                        input('You chose to be Warrior, press any key to continue')
                        Utils.warrior()
                        return Utils.world_intro()
                    elif user_character == 2:
                        print('You chose to be Wizard')
                        Utils.wizard()
                        return Utils.world_intro()
                    elif user_character == 3:
                        print('You chose to be Archer')
                        Utils.archer()
                        return Utils.world_intro()
                    else:
                        print('Please choose an option between 1,2 and 3 ')

                elif start.upper() == 'N':
                    start_game = False

        except ValueError:
            print('Something went wrong ')
        return


    @staticmethod
    def world_intro():
        pygame.mixer.stop()
        sound = 'Exploring.wav'
        sounda = pygame.mixer.Sound(sound)
        sounda.play()
        os.system('clear')

        crossroad_option = ('Village', 'Forest', 'Desert')
        print('You have to choose your desteny... ')
        index = 1
        for option in crossroad_option:
            print(f'{index} - {option}')   #
            index += 1


        path_chosen = input('Please chose your path: 1,2 or 3 --> ')
        if path_chosen == '1':
            return Utils.village()
        elif path_chosen == '2':
            return Utils.forest()
        elif path_chosen == '3':
            return Utils.desert()
        else:
            print('You have to choose one number between 1 and 3')

        return


    @staticmethod
    def village():
        os.system('clear')
        print('You are in the biggest and scary Village, mind your eye! ')
        input('Press any key to continue')
        Utils.random_enemy()
        battle.Game.start()
        return


    @staticmethod
    def forest():
        os.system('clear')
        print('You are in the biggest and scary Forest, mind your eye! ')
        input('Press any key to continue')
        Utils.random_enemy()
        battle.Game.start()
        return


    @staticmethod
    def desert():
        os.system('clear')
        print('You are in the biggest and scary Desert, mind your eye! ')
        input('Press any key to continue')
        Utils.random_enemy()
        battle.Game.start()
        return


    @staticmethod
    def warrior():
        warrior_name = battle.Player
        battle.Warrior(warrior_name)
        return warrior_name


    @staticmethod
    def wizard():
        wizard_name = battle.Player
        battle.Wizard(wizard_name)
        return wizard_name


    @staticmethod
    def archer():
        archer_name = battle.Player
        battle.Archer(archer_name)
        return archer_name


    @staticmethod
    def random_enemy():
        pygame.mixer.stop()
        sound = 'BattleFinal.wav'
        sounda = pygame.mixer.Sound(sound)
        sounda.play()
        os.system('clear')

        random_nr = random.randint(0, 2)
        if random_nr == 0:
            print('Something behind you appears! ')
            enemy.Goblin()
            print('Wrrawr, I am a Goblin, and i will poisoin YOU!!')



        elif random_nr == 1:
            print('Something behind you appears! ')
            enemy.Orc()
            print('Grrww, I am a Orc, and i will destroy YOU!!')

        elif random_nr == 2:
            print('Something behind you appears! ')
            enemy.Rat()
            print('Kiitzzs, I am a Rat, and i will eat YOU!!')

        return


# creem o CLASA UTILS pentru a stoca multiple functii utile
        # creem o metoda statica cu functia INTRO()
        # creem o variabila si atribuim in ghilimele numele fisierului audio
        # creem o variabila saunda, si o initializam cu (pygame.mixer.Sound(numele variabilei ce detine numele melodiei)
        # pornim fisierul audio
        # creem un mesaj de intro userului si il printam

# creem o metoda statica cu functia GAME_START()
        # incepem cu un TRY/EXCEPT, pentru a continua codul in cazul eventualelor erori
        # creem o variabila start, pentru a ne folosi de ea mai tarziu, continand un input de la user
        # creem o variabila game_start si ii atribuim valoare FALSE pentru a creaa o bucla while
        # daca raspunsul userului este Y, variabila game_start va deveni TRUE
        # daca raspunsul userului este N, atribuim variabilei game_start FALSE
        # iar daca userul introduce altceva, sa printam ceva userului
# creem o bucla while, folosindune de valoarea variabilei game_Start
        # daca variabila start, are valoarea Y, curatam ecranul si cerem userului sa aleaga caracterul
        # stabilim o variabila TUPLES cu caracterele valabile
        # creem o variabila pentru a stabili un index
        # creem o bucla for pentru a lista toate caracterele alaturi de un index
        # creem o variabila pentru a cere userului un raspuns, de care ne vom folosi mai tarziu
        # daca variabila este egala cu 1, importam din libraria utils functia worrior, urmata de functia world_intro
        # si retepam pentru fiecare caracter in parte
        # daca raspunsul este diferit printam ceva
        # iar daca variabila start este egala cu N, atribuim variabilei game_start valoarea FALSE
        # inchidem bucla for cu un text, daca raspunsul este diferit de Y sau N.
        # din TRY/EXCEPT, folosit except ValueError, insotit de un mesaj
        #  RETURNAM

# Creem o metoda statica cu functia WORLD_INTRO()
        # oprim fisierul audie de pe celelalte canale pentru a porni alt sunet, sa nu se suprapuna
        # creem o variabila si atribuim in ghilimele numele fisierului audio
        # creem o variabila saunda, si o initializam cu (pygame.mixer.Sound(numele variabilei ce detine numele melodiei)
        # pornim fisierul audio
        # curatam ecranul
        #stabilim prin tuples variantele ce le poate alege userul
        # [printam un mesaj]
        # stabilim un index cu valoarea 1
        # aratam variantele disponibile din tuples unele sub altele cu index crescator cu ajutorul buclei FOR
        # intr-o variabila, cerem userului un int() pentru a alege din lista tuples
        # Daca userul a scris '1', sa returnam din libraria utils functia village
        # daca userul a scris '2', sa returnam din libraria utils functia forest
        # daca userul a scris '3', sa returnam din libraria utils functia desert
        # in caz contrar, sa printam userului un mesaj de indrumare
        # si returnam

# creem o metoda statica cu functia VILLAGE(), FOREST(), DESERT()
        # curatam ecranul
        # [mesaj catre user] - village intro message, si il printam
        # aducem din libraria utils, functia random_enemy, si RETURNAM
        # si facem astfel pentru fiecare PATH(cale), in parte ('village', 'forest', 'desert').

# creem o metoda statica cu functia WARRIOR(), WIZZARD(), ARCHER()
        # Creem o variabila si cerem numele userului.
        # din modulul player, chemam functia Worrior, si atribuim parametrului variabila creata mai sus
        # si facem astfel pentru fiecare caracter in parte (warrior, wizard, archer)
        # si returnam

# creem o metoda statica, cu functia RANDOM_ENEMY()
        # importam sunetul de batalie 'BattleFinal.wav'
        # creem o variabila, si din modulul random, punem sa se aleaga un numar de la 0 la 2 (deoarece avem doar 3 inamici, iar numaratoarea incepe de la 0)
        # Daca variabila creata este egala cu numarul 0: anuntam userul cu aparitia inamicului
        # stabilim o variabila pentru a aduce din modulul enemy, un inamic
        # [mesaj catre user]
        #si repetam asa pentru fiecare inamic in parte, cu RETURN la sfarist!!!

