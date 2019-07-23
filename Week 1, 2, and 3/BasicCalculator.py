def addfunctreturn(number1,number2):
    print("I will add these")
    num1 = int(usernumber1)
    num2 = int(usernumber2)
    answer = num1 + num2
    print(f"the answer is {answer}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def subfunctreturn(number1,number2):
    print("I will subtract these")
    num1 = int(usernumber1)
    num2 = int(usernumber2)
    answer = num1 + num2
    print(f"the answer is {answer}")
    return answer
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def multfunctreturn(number1,number2):
    print("I will multiply these")
    num1 = int(usernumber1)
    num2 = int(usernumber2)
    answer = num1 * num2
    print(f"the answer is {answer}")
    return answer
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def divfunctreturn(number1,number2):
    print("I will divide these")
    num1 = int(usernumber1)
    num2 = int(usernumber2)
    answer = num1 / num2
    print(f"the answer is {answer}")
    return answer
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

while True:
    opdecision = input("do you want to add, subtract, multiply, or divide:")
    opdecision = opdecision.lower()


    if opdecision == "add":
        usernumber1 = input("enter a number: ")
        usernumber2 = input("enter another number: ")
        addfunctreturn(usernumber1, usernumber2)
    elif opdecision == "subtract":
        usernumber1 = input("enter a number: ")
        usernumber2 = input("enter another number: ")
        subfunctreturn(usernumber1,usernumber2)
    elif opdecision == "multiply":
        usernumber1 = input("enter a number: ")
        usernumber2 = input("enter another number: ")
        multfunctreturn(usernumber1,usernumber2)
    elif opdecision == "divide":
        usernumber1 = input("enter a number: ")
        usernumber2 = input("enter another number: ")
        divfunctreturn(usernumber1,usernumber2)
    else:
        print("please try again")



var1 = addfunctreturn
