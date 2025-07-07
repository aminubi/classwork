def thisFunction():
    print("This is a function")

def myFunction(n1, n2):
    print("The total is :", funcParameter(n1, n2))


#call the function
def funcParameter(num1, num2):
    total = num1 * num2
    return total

myFunction(100, 100)
#call the function
thisFunction()