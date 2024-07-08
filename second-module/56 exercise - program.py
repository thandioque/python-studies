all_ages = []

m_names = []
m_ages = []

w_ages = []

for c in range (0,4):
    name   = str(input('Enter the name: ')) 
    age    = int(input('Enter the age: '))
    gender = str(input('Enter the gender [M/F]: '))

    all_ages.append(age)
    
    if gender.upper() == 'M':
        m_names.append(name)
        m_ages.append(age)
    elif gender.upper() == 'F':
        if age < 20:
            w_ages.append(age)
    else:
        print('Another condition found !!!')

age_average = (sum(all_ages))/4
print('Age average between all ages is: {}'.format(age_average))

oldest_age = max(m_ages)
oldest_age_index = m_ages.index(oldest_age)
oldest_man = m_names[oldest_age_index]
print('{} is the oldest man who is {} years old !'.format(oldest_man.capitalize(),oldest_age))
    
print('There are {} women who are under 20 years !'.format(len(w_ages)))