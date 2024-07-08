grade1 = float(input('Type the first student grade: ')) 
grade2 = float(input('Type the second student grade: ')) 
# average = (grade1 + grade2)/2
# print('The grade average between the student grades, that is {0} and {1} is: {2:.2f}'.format(grade1,grade2,average))
print('The grade average between the student grades, that is {0:.1f} and {1:.1f} is: {2:.1f}'.format(grade1,grade2, ((grade1 + grade2)/2) ))
