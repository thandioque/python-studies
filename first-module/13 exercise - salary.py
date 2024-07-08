salary = float(input('Enter your salary: R$'))
increase = (salary + (salary * (15/100)))
print('The salary which was R${:.2f}, after the pay raise, will be: R${:.2f}'.format(salary,increase))
