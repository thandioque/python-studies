from math import radians, sin, cos, tan

angle = float(input('Enter the angle value: '))

convert = radians(angle)

print('The sine of the angle is equal to:{:.2f} \nThe cosine of the angle is equal to:{:.2f} \nThe tagent of the angle is equal to:{:.2f}'.format( sin(convert), cos(convert), tan(convert)))
