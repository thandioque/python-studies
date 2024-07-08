
from datetime import date  

current_year = date.today().year

birth_year = int(input('Enter the year that you were born: '))

age = current_year - birth_year

if age <= 9 :
   print('You are {0} years old ! So you are a little athlete.'.format(age))
elif age <= 14 :
   print('You are {0} years old ! So you are a youth athlete.'.format(age))
elif age <= 19 :
   print('You are {0} years old ! So you are a junior athlete.'.format(age))
elif age <= 25 :
   print('You are {0} years old ! So you are a senior athlete.'.format(age))
elif age > 25 :
   print('You are {0} years old ! So you are a master athlete.'.format(age))
else: 
    print('Another conditional found !')



