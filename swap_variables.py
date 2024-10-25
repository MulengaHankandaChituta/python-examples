# Python program to swap two variables

# Take inputs from the user

x = input("Enter value of x: ")
y = input("Enter value of y: ")

# create a temporary variable and swap values
temp = x
x = y
y = temp

print(f"The value of x after swapping is {x}")
print(f"The value of y after swapping is {y}")


