def calculate_product_of_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

my_list = [2, 3, 4, 5, 6]

result = calculate_product_of_list(my_list)

print("Product of the list values:", result)