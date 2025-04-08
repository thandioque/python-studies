even = []
for c in range (0,6):
    num = int(input('Enter a number: '))
    if num % 2 == 0:
        even.append(num)
print(f"User entered {len(even)} even numbers and the sum is {sum(even)}")
