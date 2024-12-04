num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

operation = input("Enter a operation: (add/sub/div/mul) ")

print("\n")
print("\n")
print("\n")

if operation == "add":
    print(num1+num2)
    print("addiotion is done")
elif operation == "sub":
 print(num1-num2)
elif operation == "mul":
    print(num1*num2)
elif operation == "div":
    if num2 != 0:
        print(num1/num2)
    else:
        print("can't divide by zero")
else:
    print("Not valid operation")