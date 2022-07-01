
# A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.
def hello():
    print('hello')

# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.
def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3] 

# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say 
# "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). 
# If the list is empty, print "My lunchbox is empty!". The function should not return anything.
def eat_lunch(mylist):
    if len(mylist) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(mylist)):
            if i == 0:
               print(f"First I eat {mylist[0]}")
            else:
               print(f"Next I eat {mylist[i]}")

# call functions above

#function one: 
hello()

# function two:
print(pack('arg1', 'arg2', 'arg3'))

# function three:
eat_lunch(["Pizza"])
eat_lunch(["eggs","banana","burger","ice cream", "Fries", "hot Dog"])
eat_lunch([])