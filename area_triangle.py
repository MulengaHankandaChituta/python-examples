# Program to find the area of a tringle

# Take inputs from the user
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# calculate the semi perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(f"The area of the triangle is {area}")

