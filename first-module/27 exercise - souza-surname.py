name = str(input('Enter full name: ')).strip()

surnamse = (len(name.strip().split())) - 1

print('The first name is: {}'.format(name.split()[0]))
print('The last surname is: {}'.format(name.split()[surnamse]))
