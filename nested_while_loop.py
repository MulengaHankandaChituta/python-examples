# program to demonstrate
# a nested while loop

i = 1
while(i<=5):
    j = 1
    while(j<=i):
        print(j,end=" ")
        j+=1
    i+=1
    print()
