from random import randint
from time import sleep
print('Enter an integer number between 0 and 5 to try to match the number which the computer is thinking.')
print('-'*100)

attempt = int(input('What number did I think ? '))

print ('Processing...')
sleep(3)
number = randint(0,5)
print('Computer: I have just thought of a number !')
print('-'*95)

if attempt == number:
    print('Congratulations you won ! {} is the number which the computer was thinking and you got it right !'.format(number))
    print("Can you discover what number the computer is thinking about again ?")
else:
    print("Try again ! Sorry, the computer won because it was thinking about the number {} and you didn't get it right".format(number))
    print("Can you discover what number the computer is thinking? Try again ! ")
print('-'*95)


