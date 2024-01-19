a = [20, 23, 82, 40, 32, 15, 67, 52]

#find the indices of even numbers
even_indices = [i for i, num in enumerate(a) if num % 2 == 0]
print("Indices of even numbers:", even_indices)

#sort the array
sorted_array = sorted(a)
print("Sorted array:", sorted_array)

#slice elements from index 3 to the end of the array
slice_1 = a[3:]
print("Slice from index 3 to the end:", slice_1)

#slice elements from index 0 to index 4
slice_2 = a[0:5]
print("Slice from index 0 to index 4:", slice_2)

#print [32, 15, 67] using negative slicing
negative_slice = a[-5:-2]
print("Negative slicing to get [32, 15, 67]:", negative_slice)