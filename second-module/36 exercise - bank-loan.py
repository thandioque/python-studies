house_price = float(input('Enter the price of the house: R$')) 
years = int(input('Enter how many years the buyer will pay: '))
buyer_salary = float(input('Enter the salary of the buyer: R$'))

monthly_installments = (house_price / (years * 12))
percentage_buyer_salary = (buyer_salary * (30/100))

if monthly_installments <= percentage_buyer_salary :
   print("Loan approved !!! Installment will cost R${0:.2f} to buy a house which costs {1:.2f} in {2} years".format(monthly_installments,house_price,years))
elif monthly_installments >= percentage_buyer_salary :
   print("Loan denied ! Installment will cost R${0:.2f} to buy a house which costs {1:.2f} in {2} years".format(monthly_installments,house_price,years))
else:
   print("Another conditional found !")


