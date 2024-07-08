from random import shuffle, sample

student1 = str(input('Enter the first student name: '))
student2 = str(input('Enter the second student name: '))
student3 = str(input('Enter the third student name: '))
student4 = str(input('Enter the fourth student name: '))

list = [student1, student2, student3, student4]

order = sample(list, k=len(list))

print('The order of the students presentation will be: {}'.format(order))
