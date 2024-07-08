number = int(input('Enter an integer: '))

division = number % 2

if division == 0:
    print('{} is an even number !'.format(number))
else: 
    print ('{} is an odd number !'.format(number))