distance = float(input('Enter the trip distance in KMs: '))
print('You are about to undertake a {}Km trip.'.format(distance))

if distance <= 200:
    short = 0.50 * distance
    print('So, as the trip is short, the price will be: R${:.2f}'.format(short))
else:
    long = 0.45 * distance
    print('So, as the trip is long, the price will be: R${:.2f}'.format(long))

# short = distance * 0.50 if distance <= 200 else distance * 0.45 
# print('The trip price will be: R${:.2f}'.format(short))
    
print('Have a good trip !')