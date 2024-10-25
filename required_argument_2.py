# This program demosntrates how
# switching of values
# also causes an error
# when it comes to required arguments

def division(num,den):
    print(num/den)

division(4,2)

division(2,4)

division(0,5)

division(5,0)