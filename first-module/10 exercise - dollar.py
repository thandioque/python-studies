money = float(input('Enter how much money you have in your wallet: R$'))

dollar = 4.89
euro = 5.23
pound = 6.03

print('You can buy ${:.2f} with R${:.2f}'.format((money/dollar), money))
print('You can buy €{:.2f} with R${:.2f}'.format((money/euro),money))
print('You can buy £{:.2f} with R${:.2f}'.format((money/pound),money))
