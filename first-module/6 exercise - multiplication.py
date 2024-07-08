num = int(input('Type a number: '))
# double = num * 2
# triple = num * 3
# square =  num ** (1/2)
# print('The double of {0} is : {1} \n The triple of {0} is : {2} \n The square root of {0} is: {3:.2f}'.format(num, double, triple, square))
print('The double of {0} is : {1} \n The triple of {0} is : {2} \n The square root of {0} is: {3:.2f}'.format(num, (num*2), (num*3), pow(num,(1/2))))
