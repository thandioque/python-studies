from  datetime import date
year = int(input('Enter a year or enter 0 to analyse the current year: '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('{} is a leap year !'.format(year))
else:
    print("{} isn't a leap year".format(year))

# print('Number of remainders when the {} year was divided by 4: {}'.format(year,four))
# print('Number of remainders when the {} year was divided by 100: {}'.format(year,hundread))
# print('Number of remainders when the {} year was divided by 400: {}'.format(year,four_hundread))