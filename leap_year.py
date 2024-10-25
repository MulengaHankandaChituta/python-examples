# Python program to check if
# a year is a leap year

# prompt user to enter a year
year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year

if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year")

# if not divided by means not a century year
# year divided by 4 is a leap year

elif (year % 4 == 0) and (year % 100 != 0):
    print(f"{year} is a leap year")

# if not divided by both 400 (century year) and 4
# year is not a leap year

else:
    print(f"{year} is not a leap year")
    


           

           
