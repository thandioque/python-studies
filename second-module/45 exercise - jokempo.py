# from random import choices
from random import randint

from time import sleep

print('''See the hand symbols:
[1] Rock
[2] Paper
[3] Scissors''')
user_symbol = int(input('Choose the user option: ')) 

unid = ('rock','paper','scissors')
machine_symbol = '{}'.format(unid[randint(1,3)])

# machine_symbol = choices(['rock', 'paper', 'scissors'])

if user_symbol in [1,2,3]:

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    
    if machine_symbol == 'rock':
        if user_symbol == 1:
            print('Draw ! User and machine chose the same symbols.')
        elif user_symbol == 2:
            print('Congratulations, the user won! User chose paper and the machine chose rock.')
        elif user_symbol == 3:
            print('Opsss, the machine won! Machine chose the rock and the user chose scissors.')
        else: 
            print('Another conditional found when the machine chose rock !')    
    elif machine_symbol == 'paper':
        if user_symbol == 1:
            print('Opsss, the machine won! Machine chose paper and user chose rock.')
        elif user_symbol == 2:
            print('Draw ! User and machine chose the same symbols.')
        elif user_symbol == 3:
            print('Congratulations, the user won! User chose scissors and the machine chose paper.')
        else: 
            print('Another conditional found when the machine chose paper !')  
    elif machine_symbol == 'scissors':
        if user_symbol == 1:
            print('Congratulations, the user won! User chose rock and the machine chose scissors')
        elif user_symbol == 2:
            print('Opsss, the machine won! Machine chose scissors and the user chose paper.')
        elif user_symbol == 3:
            print('Draw ! User and machine chose the same symbols.')
        else: 
            print('Another conditional found when the machine chose scissors !')
    else: 
       print('Another conditional found between machine symbols!')
else: 
    print('Invalid option !!! Try again...')  