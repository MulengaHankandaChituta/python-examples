# program to demonstrate
# a simple python function

def welcome(name):
    '''This function takes the name as input and 
    welcomes the person'''
    print("Hello, ",name,"Welcome to PythonGeeks!")

welcome("mulenga")
print("The docstring of the welcome function is: ")
print(welcome.__doc__)

print("The type of the docstring is",type(welcome.__doc__))