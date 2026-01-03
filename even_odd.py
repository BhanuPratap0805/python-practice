def is_even(number):
    return number % 2 == 0

try:
    num = int(input("Enter a number: "))
    if is_even(num):
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Invalid input")
