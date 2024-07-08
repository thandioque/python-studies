product = float(input('Enter the product price: R$'))
quantity = int(input('Enter the installments number: '))
installments = quantity * (product * 8/100)
increase = product + installments 

print('The price of the product is R${}, if the payment is in cash the value would be R${} and if the payment is in installments the value would be R${}'.format(product,(product - (product * 10/100)),increase))
