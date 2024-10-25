# program to demonstrate variable number of arguments
# when we do not know the number of arguments
# to be passed we can use the function
# of variable arguments
# they are named under the same name and 
# are preceeded by an Asterisk(*)

def values_of_list(*varlist):
    for i in varlist:
        print(i)

values_of_list(3,4)

values_of_list('a',6,9.0,'y')