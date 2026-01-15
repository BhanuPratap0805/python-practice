first_number = float(input("What's the first number: "))

operation = """+
-
*
/"""
print(operation)
operation_used = input("Pick an operation: ")

second_number = float(input("What's the next number: "))

def calculator(x,y):
    if operation_used == "+":
        return x + y
    elif operation_used == "-":
        return x - y
    elif operation_used == "*":
        return x * y
    elif operation_used == "/":
        return x/y

print("The solution is: ", calculator(first_number,second_number))