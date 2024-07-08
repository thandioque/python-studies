from datetime import date

current_year = date.today().year

full_array = []

minor_array = []

adults_array  = []

for c in range (0,7):
    birth_year = int(input('Enter a year of birth: '))
    age = current_year - birth_year 
    full_array.append(age)
    age_array = full_array[c:c+1]
    if age_array[0] < 18:
        minor_array.append(age_array[0])
    elif age_array[0] >= 18:
        adults_array.append(age_array[0])
    else:
        print('Another conditional found !')
minors_count = len(minor_array)
adults_count = len(adults_array)
print('Numbers of minors: {} '.format(minors_count))
print('Numbers of adults: {} '.format(adults_count))
