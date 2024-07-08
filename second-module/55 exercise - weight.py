all_weights = []

for c in range (0,5):
    weight = float(input('Enter the weight in kg: ')) 
    all_weights.append(weight)
    
greater = max(all_weights)
lower = min(all_weights)
print('Greater weight between the list {} is: {}'.format(all_weights,greater))
print('Lower weight between the list {} is: {}'.format(all_weights,lower))


