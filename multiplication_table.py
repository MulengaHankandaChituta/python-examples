# program to display a multiplication table
# from 1 to 10

# take input from the user

num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 101):
    print(num, 'x', i, '=', num*i)
