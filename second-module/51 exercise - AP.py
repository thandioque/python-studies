# My way

# first_ap = int(input('Enter the first AP term: '))
# ratio    = int(input('Enter the ratio: '))

# progression = []

# progression.append(first_ap)

# for c in range (0,9):

#     calc = progression[c]+ratio
#     progression.append(calc)

# int_terms = (' -> '.join(map(str, progression)))
# print("Arithmetic Progression's 10 first terms: {}".format(int_terms))

# Mathematically way

first = int(input('Enter the first AP term: '))
ratio = int(input('Enter the ratio: '))
tenth = first + (10 - 1) * ratio

for c in range (first, tenth + ratio, ratio):
    print(c)