print("Welcome to David's Code >:C")

num1 = int(raw_input("Enter a number: "));
num2 = int(raw_input("Enter a 2nd number: "));
selection = str(raw_input("Enter a selection: "))

def myAddFunction(add1, add2):
    sum = add1 + add2
    return sum

def mySubFunction(sub1, sub2):
    difference = sub1 - sub2
    return difference

def myMultFunction(mult1, mult2):
    product = mult1 * mult2
    return product

if selection.upper() == "ADD":
    print("Here is the sum: " + str(myAddFunction(num1, num2)))
elif selection.upper() == "SUBTRACT":
     print("Here is the difference: " + str(mySubFunction(num1, num2)))
elif selection.upper() == "MULTIPLY":
     print("Here is the product: " + str(myMultFunction(num1, num2)))
