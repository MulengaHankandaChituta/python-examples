# Program to check if number is odd or even
# a number is even if division by 2 gives remainder of 0
# if remainder is 1 number is odd

num = int(input("Enter a number: "))
if (num % 2) == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
