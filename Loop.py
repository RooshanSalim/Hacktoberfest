# Calculate the sum of all of the elements in a list
def sum_list(list):
    total = 0
    for element in list:
        total += element
    return total

# Find the largest number in a list
def find_largest_number(list):
    largest_number = list[0]
    for element in list:
        if element > largest_number:
            largest_number = element
    return largest_number

# Print all of the even numbers from 1 to 10
for i in range(2, 11, 2):
    print(i)
