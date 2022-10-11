# Создайте программу для игры в ""Крестики-нолики"".

from os import system
from random import randint

# Игровое поле в консоли
def array_console(arr):
    for i in range(len(arr)):
        print(arr[i])


# Проверка на выигрыш
def check_winner(array, player_tag):
    count = [0,0,0,0]
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[j][i] == player_tag:
                count[0] += 1
            if array[i][j] == player_tag:
                count[1] += 1
        if count[0] != len(array):
            count[0] = 0
        else:
            return count[0]
        if count[1] != len(array):
            count[1] = 0
        else:
            return count[1]
        if array[i][i] == player_tag:
            count[2] += 1
        if array[len(array)-1-i][i] == player_tag:
            count[3] += 1
    for i in range(len(count)):
        if count[i] == len(array):
            return count[i]
    return 0


# Защита ячеек от повторного ввода
def check_cell(array, position):
    if position[0] == 0 and position[1] == 0:
        position = [1,1]
    if array[position[0]-1][position[1]-1] == '_':
        return True
    else:
        return False

# Проверка полного заполнения поля
def check_field(arr):
    check = False
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '_':
                check = True
                return check
    return check

clear = lambda: system('cls')

# Создание игрового поля нужного размера
def field_creation():
    size = 0 
    while size < 3 or size > 5:
        size = int(input('"Крестики-нолики"\nЗадайте размер игрового поля \nВведите цифру от 3 до 5 ->  '))
    array = [['_']*size for i in range(size)]
    return array

# Игровой процесс
def game_process(array):
    game_field = array
    select = randint(0,1)
    players = ['X','O']
    move = [0,0]
    end = 0
    while end != len(game_field):
        clear()
        array_console(game_field)
        print(f'Ход {select+1}-го игрока')
        while move[0] < 1 or move[0] > len(game_field) or move[1] < 1 or move[1] > len(game_field) or check_cell(game_field,move)==False:
            move = [int(i) for i in (input("Чтобы сделать ход - \nвведите номер строки и столбца через пробел -> ").split())]
            if check_field(game_field) == False:
                break
        game_field[move[0]-1][move[1]-1] = players[select]
        array_console(game_field)
        end = check_winner(game_field,players[select])
        if end !=len(game_field):
            if check_field(game_field) == False:
                select = 2
                clear()
                array_console(game_field)
                return select
            select = len(players)-1-select
            move=[0,0]
    clear()
    array_console(game_field)
    return select
    

def General():
    clear()
    gamein_field = field_creation()
    winner = game_process(gamein_field)+1
    if winner == 3:
        print('Вы сыграли вничью')
    else:
        print(f'Победил {winner}-й игрок')
General()