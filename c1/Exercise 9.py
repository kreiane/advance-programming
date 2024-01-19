# Create an int list with 10 values
integer_list = [1, 2, 3, 5, 4, 8, 6, 7, 10, 9]

# Output the list using a for loop
print("List elements:")
for value in integer_list:
    print(value, end=" ")

# Output the highest and lowest value
print("\nHighest value:", max(integer_list))
print("Lowest value:", min(integer_list))

# Sort the elements in ascending order
integer_list.sort()
print("Sorted in ascending order:", integer_list)

# Sort the elements in descending order
integer_list.sort(reverse=True)
print("Sorted in descending order:", integer_list)

# Append two elements 
integer_list.append(20)
integer_list.append(11)

# Print the list after appending
print("List after appending two elements:", integer_list)