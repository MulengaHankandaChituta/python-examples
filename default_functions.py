# program to demonstrate the
# use of default arguments

def avg_mark(sub1,sub2,sub3,sub4=0,sub5=0):
    avg=(sub1+sub2+sub3+sub4+sub5)/5
    print("The average of the marks in the 5 subjects is ",avg)

avg_mark(63,78,96,84,87)

avg_mark(45,34,65,53)