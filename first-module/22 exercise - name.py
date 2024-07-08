name = str(input('Enter your full name: ')).strip()
letters = ''.join(name.split()) 

print('That is your name in capital letters: {}'.format(name.upper()))
print('That is your name in lower case letters: {}'.format(name.lower()))
print('The letters quantity without considering spaces is: {}'.format(len(letters)))
# print('The letters quantity without considering spaces is: {}'.format(len(name) - (name.count(' '))))        
print('The letters quantity of the first name is: {}'.format(len(name.split()[0])))
# print('Your first name is {} and it has {} letters.'.format(name.split()[0], len(name.split()[0])))

