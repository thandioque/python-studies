speed = float(input('Enter the car speed in KMs that you were driving: '))

if speed > 80:
    fine = ( speed - 80) * 7 
    print( 'You will be fined ! You have exceeded the permitted speed limit of 80Km/h \nThe traffic fine value is: R${:.2f}'.format(fine))
print('Drive safely !')
