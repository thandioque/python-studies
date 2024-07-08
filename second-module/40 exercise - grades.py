grade1 = float(input('Enter your first exam grade: ')) 
grade2 = float(input('Enter your second exam grade: '))

grade_avg=round((grade1+grade2)/2, 1)

print('Average between {} and {} grades is {:.1f}'.format(grade1,grade2,grade_avg))

if grade_avg < 5:
    print("Student failed !".format(grade_avg))
elif 7 > grade_avg >= 5:
    print("Student has is in recovery !".format(grade_avg))
elif grade_avg >= 7.0 :
    print("Student passed !!!".format(grade_avg))
else: 
    print("Another conditional found !")