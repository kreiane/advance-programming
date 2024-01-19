import math

# Function to calculate the area of a square
def calculate_square_area():
    side_length = float(input("Enter the side length of the square: "))
    area = side_length ** 2
    print(f"The area of the square is {area} square units.")

# Function to calculate the area of a circle
def calculate_circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print(f"The area of the circle is {area} square units.")

# Function to calculate the area of a triangle
def calculate_triangle_area():
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is {area} square units.")

while True:
    print("Choose an option:")
    print("1: Calculate the area of a square")
    print("2: Calculate the area of a circle")
    print("3: Calculate the area of a triangle")
    print("4: Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        calculate_square_area()
    elif choice == '2':
        calculate_circle_area()
    elif choice == '3':
        calculate_triangle_area()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")