# Program to convert kilometers to miles

kilometers = float(input("Enter a value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print(f"{kilometers} kilometers is equal to {miles} miles")
