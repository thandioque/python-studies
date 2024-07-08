from emoji import emojize
from time import sleep

fireworks = emojize(':fireworks:') 
explosion = emojize(':collision:') 

for c in range (10, -1, -1):
    print(c)
    sleep(1)
print('{} FIIIIIIIIU !'.format(fireworks)*5, end='')
print('{} BOOOOOOOOOOOOM !!!'.format(explosion)*5)

