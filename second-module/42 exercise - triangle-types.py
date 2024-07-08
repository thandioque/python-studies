length1 = float(input('Enter the first straight length in cm: ')) 
length2 = float(input('Enter the second straight length in cm: '))
length3 = float(input('Enter the third straight length in cm: '))

if length1 + length2 > length3 and length3 + length1 > length2 and length2 + length3 > length1:
    print('Lenghts makes a triangle.', end=' ')    
    if length1 == length2 == length3:
        print('Since all lengths are equal, so it is an equilateral triangle !')
    elif length1 == length2 or length1 == length3 or length2 == length3 :
        print('Since two lengths are equal, so it is an isosceles triangle !')
    elif length1 != length2 != length3 != length1 :
        print('Since all lengths are different, so it is a scalene triangle !')
    else:
        print("Another conditional found !")
else: 
    print("Doesn't make a triangle !!!")