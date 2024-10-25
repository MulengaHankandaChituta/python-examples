# you can set a variable argument
# with another type of argument
# as shown below

def langs(name,*listlangs):
    print("The languages ", name," can speak are:")
    for lan in listlangs:
        print(lan)

langs('mulenga','English','Bemba')

langs('rachael','English','Bemba','Greek')