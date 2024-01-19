with open("numbers.txt", "r") as file:
    numbers_content = file.readlines()

numbers_list = [int(number.strip()) for number in numbers_content]

for number in numbers_list:
    print(number)