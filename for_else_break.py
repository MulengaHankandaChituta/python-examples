# for loop with else statement and break statement

for i in range(1,6):
    print(i**2)
    if(i==5): break
else:
    print("This will execute only when the for loop does not run at least one time")
