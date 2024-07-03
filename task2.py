a = int(input("Enter your first Number : "))
b = int(input("Enter your second Number : "))
op = input("Enter The symbol of operation you want to perform (+ , - , * , /) : ")
if op == "+":
    print(f"The Addition of {a} and {b} is {a+b}")
elif op == "-":
    print(f"The Subtraction of {a} and {b} is {a-b}")
elif op == "*":
    print(f"The Multiplication of {a} and {b} is {a*b}")
elif op == "/":
    if b==0 :
        print(f"Sorry Any number cannot be divided by Zero")
    else : 
        print(f"The Division of {a} and {b} is {a/b}")
else :
    print("Please Enter any one of the operation given in the brackets and try again !")