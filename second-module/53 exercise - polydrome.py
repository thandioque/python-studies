# My way

# phrase = str(input('Enter a phrase: ')).strip()

# formated = ''.join(phrase.split())

# count_formated = len(formated)

# end_range = count_formated - 1

# array = []

# for c in range (end_range, -1, -1):
#     reverse = formated[c:c+1]
#     array.append(reverse)
#     polydrome = ''.join(array)
# if formated == polydrome:
#     print('''This is a palindrome phrase!
# The sentence {} in reverse is equal to {}'''.format(formated,polydrome))
# else:
#     print("{} isn't a polydrome".format(phrase))

# Other way

# phrase = str(input('Enter a phrase: ')).strip().upper()

# words = phrase.split()

# concatenater = ''.join(words)

# reversed = ''

# for letter in range(len(concatenater) - 1, -1, -1 ):
#     reversed += concatenater[letter]
# if reversed == concatenater:
#     print('{} in reverse is equal to {} so this is a palindrome phrase!'.format(concatenater,reversed))
# else:
#     print('{} in reverse isn`t equal to {} so this isn`t a palindrome phrase!'.format(concatenater,reversed))

# Without for

phrase = str(input('Enter a phrase: ')).strip().upper()

words = phrase.split()

p_concatenater = ''.join(words)

reversed = phrase[::-1].split()

r_contatenater = ''.join(reversed)

if r_contatenater == p_concatenater:
    print('{} in reverse is equal to {} so this is a palindrome phrase!'.format(p_concatenater,r_contatenater))
else:
    print('{} in reverse isn`t equal to {} so this isn`t a palindrome phrase!'.format(p_concatenater,r_contatenater))