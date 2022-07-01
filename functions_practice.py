
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

# adding another function as a bonus with a while loop, I want to the same type of functionality as above.
def eat_dinner(dinner):
    i = 0
    if len(dinner) == 0:
        print("My dinner plate is empty!")
        
    while len(dinner) > 0:
        if i == 0:
            print(f"for diner first I eat {dinner[0]}")
        else:
            print(f"Next for dinner I eat {dinner[i]}")
        i = i + 1
        # when the index reach the number of len(dinner) then break from loop else you will get an error
        if i == len(dinner):
            break

# call functions above

#function one: 
hello()

# function two:
print(pack('arg1', 'arg2', 'arg3'))

# function three:
eat_lunch(["Pizza"])
eat_lunch(["eggs","banana","burger","ice cream", "Fries", "hot Dog"])
eat_lunch([])

# run dinner function
eat_dinner(['Lobster', 'Maui Maui', 'BlueFin'])
eat_dinner([]) 
