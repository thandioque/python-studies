remains_list = []

num = int(input('Enter a number: '))

for c in range (1,num+1):
    remains_calc = num%c
    remains_list.append(remains_calc)

remains_counting = remains_list.count(0)

if remains_counting == 2:
    print('{} is a prime number because it can only be divided by itself and one.'.format(num))
elif remains_counting > 2 or remains_counting < 2:
    print("{} isn't a prime number and has {} divisors.".format(num,remains_counting))
else:
    print('Another conditional found !')
