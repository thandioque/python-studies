# My way

# remains_list = []

# num = int(input('Enter a number: '))

# for c in range (1,num+1):
#     remains_calc = num%c
#     remains_list.append(remains_calc)

# remains_counting = remains_list.count(0)

# if remains_counting == 2:
#     print('{} is a prime number because it can only be divided by itself and one.'.format(num))
# elif remains_counting > 2 or remains_counting < 2:
#     print("{} isn't a prime number and has {} divisors.".format(num,remains_counting))
# else:
#     print('Another conditional found !')

# Other way

num = int(input('Enter a number: '))
counter = 0

for c in range (1, num + 1):
    if num % c == 0:
        print('\033[1;32m{}'.format(c), end='')
        counter += 1
    else:
        print ('\033[1;31m{}'.format(c), end='')
print ('\n\033[m{} was divisible by {} numbers'.format(num,counter))
if counter == 2:
    print('So {} is a prime number'.format(num))
else:
    print('So {} isn`t a prime number'.format(num))