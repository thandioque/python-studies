salary = float(input('Enter your salary: R$'))

if salary > 1250:
    increase = (salary + (salary * (10/100)))
    print('Your salary with the increase salary will be: {:.2f}'.format(increase))
else: 
    increase = (salary + (salary * (15/100)))
    print('Your salary with the incerase salary will be: {:.2f}'.format(increase))