# Write code that finds the smallest number in a list of numbers

numbers = [5, 9, 14, 3, 11]

smallest = numbers[0]
for n in numbers:
    if n < smallest:
        smallest = n

print("The smallest number is:", smallest)