decimal_number = int(input('Enter an integer number: ')) 
print('''Select a conversion basis :
[1] Binary conversion
[2] Octal conversion
[3] Hexadecimal conversion''')
conversion_basis = int(input('Enter a option : '))


if conversion_basis == 1 :
   print('Decimal number {0} converted to binary is: {1}'.format(decimal_number, bin(decimal_number)[2:]))
elif conversion_basis == 2 :
   print('Decimal number {0} converted to octal is: {1}'.format(decimal_number, oct(decimal_number)[2:]))
elif conversion_basis == 3 :
   print('Decimal number {0} converted to hexadecimal is: {1}'.format(decimal_number, hex(decimal_number)[2:]))
elif conversion_basis not in [1,2,3]:
   print('Invalid option! Try again...')
else: 
    print("Another conditional found !")



