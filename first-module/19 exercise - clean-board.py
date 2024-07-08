from random import choice 

student1 = str(input('Enter the first student name: '))
student2 = str(input('Enter the second student name: '))
student3 = str(input('Enter the third student name: '))
student4 = str(input('Enter the fourth student name: '))

print('The student chosen to clean the board is: {}'.format(choice([student1,student2,student3,student4])))
