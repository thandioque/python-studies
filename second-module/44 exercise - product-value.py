normal_product_value = float(input('Enter the product value: R$')) 

print('''See payment methods: 
[1] cash or check 
[2] cash on credit card
[3] two installments on credit card
[4] three or more installments on credit card)''')
payment_condition = int(input('Enter the option: '))

if payment_condition == 1 :
    first_condition = (normal_product_value - (normal_product_value * (10/100)))
    print('Normal product value is R${0:.2f},but paying by cash or check, the price that should be paid is: R${1:.2f}'.format(normal_product_value,first_condition)) 
elif payment_condition == 2 :
    second_condition = (normal_product_value - (normal_product_value * (5/100)))
    print('Normal product value is R${0:.2f},but paying by cash on credit card, the price that should be paid is: R${1:.2f}'.format(normal_product_value,second_condition)) 
elif payment_condition == 3 :
    third_condition = normal_product_value / 2
    print('Product price that should be paid is: 2x of R${0:.2f} interest-free installments, which results in a value of: R${1:.2f}'.format(third_condition,normal_product_value)) 
elif payment_condition == 4 :
    fourth_condition = (normal_product_value + (normal_product_value * (20/100)))
    installments = int(input('Enter installments number: '))
    product_interest_value = fourth_condition / installments
    print('Normal product value is R${0:.2f},but paying more than 3 installments on credit card, the price that should be paid is: {1}x of R${2:.2f} with interest, which results in a value of: R${3:.2f}'.format(normal_product_value, installments, product_interest_value, fourth_condition)) 
elif payment_condition not in [1,2,3,4]:
   print('Invalid payment method option! Try again...')
else: 
    print('Another conditional found !')