numbers = [18, 4, 25, 9, 31, 2]


min_val = numbers[0]
max_val = numbers[0]

for num in numbers:
    if num < min_val:
        min_val = num  
    elif num > max_val:
        max_val = num  

print("Minimum Value:", min_val)
print("Maximum Value:", max_val)
