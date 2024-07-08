price = float(input('Enter the product price: R$'))
discount = (price - (price * (5/100)))
print('The product which cost R${:.2f} with 5% discount will be: R${:.2f}'.format(price,discount))
