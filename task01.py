# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

from os import system
from random import randint
from math import floor


# Начало игры
def start_menu():
    print("""
    Welcome to

    "2021 Bloody Candies on the Cursed Black Table",
    Stranger

    Select the game mode:

    1. Single player
    2. Multy player
    """)
    a = 0
    while a<1 or a>2:
        a = int(input("    Please type 1 or 2 to select the game mode -> "))
    return a

# Multy player - Режим двух игроков (пользователей)     
def multy_player(candy):
    candies = candy
    
    players = [0,0]
    move = 29
    select = randint(0,1)
    print('There are 2021 Bloody Candies on the Cursed Black Table')
    while candies != 0:
        while move > 28:
            print(f'Player {select+1} make your turn.')
            move = int(input(f'How many candies will you take? Max you can take 28    -   There is {candies} candies.  '))    
        if candies-move >= 0:
            players[select] += move
            candies -= move
            if candies != 0:
                select = len(players)-1-select
        move = 29
    return select+1

# Single player - игра против бота
def single_player(candy):
    candies = candy

    players = [0,0]
    move = 29
    select = randint(0,1)
    print('There are 2021 Bloody Candies on the Cursed Black Table')
    while candies!=0:
        while move>28:
            if select == 1:
                print(f'Player make your turn!')
                move = int(input(f'How many candies will you take? Max you can take 28    -   There is {candies} candies.  ')) 
                print('___________________________________________')
            else:
                print('Machine is making its turn!')
                if candies>=28:
                    move = randint(1,28)
                    print(f'Machine took {move} candies.                      -   There are {candies-move} candies left.\n___________________________________________')
                else:
                    move = candies
                    print(f'Machine took {move} candies.                      -   There are {candies-move} candies left.\n___________________________________________')

        if candies-move >= 0:
            players[select] += move
            candies -= move
            if candies != 0:
                select = len(players)-1-select
        move=29
    return select+1


# Игровой процесс
def game_process(choice):
    total_candies = 2021
    if choice == 2:
        win = multy_player(total_candies)
    elif choice == 1:
        win = single_player(total_candies)
    
    return win

clear = lambda: system('cls')

# Вывод финального экрана
def final_output(choice,player):
    type = choice
    winner = player
    if type == 1 or winner == 1:
        print('Player has been defeated by the heartless Machine!')
    elif type == 2:
        print(f'Player {winner} WON! Congratulations!')
    elif type == 3 or winner == 1:
        print('Player WON! Praise Player the Smartest Man Alive!')

# Игра
def General():
    clear()
    type = start_menu()
    winner = game_process(type)
    final_output(type,winner)

General()     