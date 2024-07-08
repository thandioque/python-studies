weight = float(input('Enter the weight in kg: ')) 
height_m = float(input('Enter the height in m: '))

# conversion_cm = height_m / 100

bmi = weight/(height_m ** 2)

if bmi < 18.5 :
    print('BMI is equal to {0:.1f} so the person is underweight !'.format(bmi)) 
elif 25 > bmi >= 18.5 :
    print ('BMI is equal to {0:.1f} so the person with the ideal weight !'.format(bmi)) 
elif 30 > bmi >= 25 :
    print ('BMI is equal to {0:.1f} so the person is with overweight !'.format(bmi)) 
elif 40 > bmi >= 30 :
    print ('BMI is equal to {0:.1f} so the person is with obesity !'.format(bmi))
elif bmi >= 40:
    print ('BMI is equal to {0:.1f} so the person is with morbid obesity!'.format(bmi)) 
else: 
    print('Another conditional found !')
