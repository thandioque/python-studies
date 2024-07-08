first_ap = int(input('Enter the first AP term: '))
ratio    = int(input('Enter the ratio: '))

progression = []

progression.append(first_ap)

for c in range (0,9):
   
    calc = progression[c]+ratio
    progression.append(calc)
print("Arithmetic Progression's 10 first terms: {}".format(progression))
