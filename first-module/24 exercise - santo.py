city = str(input("Enter a city's name: ")).strip()

# print('Does this city begin with the SANTO name ?\nAnswer: {}'.format(city[:5].upper() == 'SANTO'))

print('Does this city begin with the SANTO name ?\nAnswer: {}'.format('SANTO' in city.upper().split()[0]))
