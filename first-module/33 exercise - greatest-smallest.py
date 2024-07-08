first_number = int(input('Enter an integer: '))
second_number = int(input('Enter a second integer: ')) 
third_number = int(input('Enter a third integer: '))
# Checking which is the greatest
greatest = first_number
if second_number > first_number and second_number > third_number:
    greatest = second_number
if third_number > first_number and third_number > second_number:
    greatest = third_number
# Checking which is the smallest
smallest = first_number
if second_number < first_number and second_number < third_number:
    smallest = second_number
if third_number < first_number and third_number < second_number:
    smallest = third_number
# Checking when two variables are equal
if first_number > second_number and second_number == third_number:
    greatest = first_number
    smallest = second_number
if first_number < second_number and second_number == third_number:
    greatest = second_number 
    smallest = first_number
print('{} is the greatest number !'.format(greatest))
print('{} is the smallest number !'.format(smallest))

# # Two Equals
# if first_number == second_number:
#     if third_number < first_number :
#         greatest = first_number      
#     if third_number > first_number :
#         smallest = first_number
# if second_number == third_number:
#     if first_number < second_number:
#         greatest = second_number   
#     if first_number > second_number:
#         smallest = second_number
# if third_number == first_number:
#     if second_number < third_number :
#         greatest = third_number 
#     if second_number > third_number :
#         smallest = third_number
# # Greatest
# if first_number > second_number and first_number > third_number:
#     greatest = first_number 
# if second_number > first_number and second_number > third_number:
#     greatest = second_number
# if third_number > first_number and third_number > second_number:
#     greatest = third_number
# # Smallest
# if first_number < second_number and first_number < third_number:
#     smallest = first_number
# if second_number < first_number and second_number < third_number:
#     smallest = second_number 
# if third_number < first_number and third_number < second_number:
#     smallest = third_number
# print('{} is the greatest number !'.format(greatest))
# print('{} is the smallest number !'.format(smallest))
# #Equals
# if first_number == second_number and first_number == third_number:
#     print("There isn't greater or smallest number ")