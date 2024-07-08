number = str(input('Enter a number between 0 and 9999: ').strip())

# print('Ones: {}'.format(number[3]))
# print('Tens: {}'.format(number[2]))
# print('Hundreds: {}'.format(number[1]))
# print('Thousands: {}'.format(number[0]))

print('{:-^50}'.format('Math operation'))

print ( 'Ones: {}'.format(int(number) % 10 ))
print ( 'Tens: {}'.format(int(number) // 10 % 10 ))
print ( 'Hundreds: {}'.format(int(number) // 100 % 10 ))
print ( 'Thousands: {}'.format(int(number) // 1000)) 
