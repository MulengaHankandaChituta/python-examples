# program to demonstrate a required argument
# this argument is passed in a certain order
# When we call the function we need to pass
# the same number of arguments in the function definition

def greatest(n1,n2,n3):
    if(n1>n2 and n1>n3):
        print(n1," is the greatest of the three numbers")
    elif(n2>n1 and n2>n3):
        print(n2," is the greatest of the three numbers")
    else:
        print(n3," is the greatest of the three numbers")

greatest(5,2,9)

greatest(1,6,)

greatest(2,9,5)
