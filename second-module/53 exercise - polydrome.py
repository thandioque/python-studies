phrase = str(input('Enter a phrase: ')).strip()

formated = ''.join(phrase.split())

count_formated = len(formated)

end_range = count_formated - 1

array = []

for c in range (end_range, -1, -1):
    reverse = formated[c:c+1]
    array.append(reverse)
    polydrome = ''.join(array)
if formated == polydrome:
    print('''This is a palindrome phrase!
The sentence {} in reverse is equal to {}'''.format(formated,polydrome))
else:
    print("{} isn't a polydrome".format(phrase))