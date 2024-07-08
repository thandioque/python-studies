phrase = str(input('Enter a phrase: ')).upper().strip()

unified = (''.join(phrase.split()))

print("How many letters 'a' are there in the phrase ?\nAnswer: {}".format(phrase.count('A')))
# print('Where in the index does it appear for the first time?\nAnswer: {}'.format(phrase.find('A')))
print('Where does it appear for the first time?\nAnswer: {}'.format(phrase.find('A')+1))
# print('Where in the index does it appear for the last time ?)\nAnswer: {}'.format(unified.rfind('A')))
print('Where does it appear for the last time ?\nAnswer: {}'.format(unified.rfind('A')+1))
