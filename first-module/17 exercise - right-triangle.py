from math import hypot
# from math import sqrt

opposite = float(input('Enter the length of the opposite side: '))
triangle = float(input('Enter the length of the right triangle: ')) 

# length = (opposite**2) + (triangle**2)

# hypotenuse = (length ** (1/2)) 

# hypotenuse = sqrt(length)

hypotenuse = hypot(opposite, triangle)


print('The length of the hypotenuse is equal to:{:.2f}'.format(hypotenuse))

# print('The number {} has an integer part equal to {}'.format(float,floor(float)))
