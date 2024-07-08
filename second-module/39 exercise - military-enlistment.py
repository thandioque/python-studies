
from datetime import date

current_year = date.today().year

print('''Genders:
[M] Masculine
[F] Feminine''')

gender = str(input('Enter your gender: '))

if gender == 'M':

   birth_year = int(input('Enter your birthday year: '))

   age = current_year - birth_year

   print('Anyone born in {0} is {1} years old in {2} !'.format(birth_year,age,current_year))

   if age == 18 :
      print("It's time to enlist, you must go immediately !!!")
   elif age < 18 :
      print('Time left until the deadline in years: {0}\nYou will still enlist in {1}.'.format(18 - age, current_year + (18 - age)))
   elif age > 18 :
      print('Time past the deadline in years: {0}\nThe time to enlist has passed ! You should have enlisted in {1}.'.format(age - 18, current_year - (age - 18)))
   else: 
       print('Another conditional found in masculine gender !')
elif gender == 'F':
   print("You don't need to enlist !")
elif gender not in ['F','M']:
   print('Invalid option! Try again...')
else:
   print('Another conditional found')
