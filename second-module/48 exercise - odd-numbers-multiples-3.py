three_multiples = []

# Defines a range of odd numbers between 1 and 51 
for c in range (1,501,2):
    # Creates a variable that stores the remainders of the numbers within the created range
    leftovers = c % 3
    # Create a conditional to print only numbers that are multiples of 3 (Numbers that when divided by 3 haven't remainder)
    if leftovers == 0:
    # Prints numbers multiples of 3
        three_multiples.append(c)
total = sum(three_multiples)

print('Sum of all three odd multiples between the range 1 and 500 is: {}'.format(total))