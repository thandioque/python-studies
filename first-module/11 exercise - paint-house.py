width = float(input('Enter the wall width in meters: ' ))
height = float(input('Enter the wall height in meters: '))

area = (height * width)
# Each liter of paint paints 2 meters per area  
liter = area / 2 
paints = int(liter / 2)
print('Your wall is {0}m in width and {1}m in lenght, so it has {2}m² in area'.format(width,height,area))
print('You will need {0}l which is approxiamte {1} paint cans to completely fill the wall'.format(liter,paints))
