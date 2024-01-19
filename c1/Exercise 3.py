side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("These side lengths can form a triangle.")
    if side1 == side2 == side3:
        print("This is an Equilateral triangle.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("This is an Isosceles triangle.")
    else:
        print("This is a Scalene triangle.")
else:
    print("These side lengths cannot form a triangle.")

