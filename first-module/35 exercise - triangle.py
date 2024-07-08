length1 = float(input('Enter the first straight length in cm: ')) 
length2 = float(input('Enter the second straight length in cm: '))
length3 = float(input('Enter the third straight length in cm: '))

if length1 + length2 > length3 and length3 + length1 > length2 and length2 + length3 > length1:
    print('The lenghts makes a triangle')
else: 
    print("Doesn't make a triangle")

# print('Adding {} + {} = {}. Is {} greater than {} ?'.format(length1,length2,first,first,length3))
# print('Adding {} + {} = {}. Is {} greater than {} ?'.format(length3,length1,opposites,opposites,length2) )
# print('Adding {} + {} = {}. Is {} greater than {} ?'.format(length2,length3,last,last,length1))