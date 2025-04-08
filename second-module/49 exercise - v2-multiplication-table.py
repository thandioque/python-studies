
num = int(input('Enter a number: '))

print('-'*10)
for c in range (1,11):
    multi_table = num * c
    print('{0} x {1} = {2}'.format(num, c, multi_table))
print('-'*10)