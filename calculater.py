import math

x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))

print("Choose an operation: Addition | 	Sub | Division | power | Multiplication | sin | cos")

z = input("Enter your operation: ")

match z:
    case "Addition":
        result = x + y
        print("Your Addition is", result)

    case "	Sub":
        result = x - y
        print("Your subtraction is", result)

    case "power":
        result = x ** y
        print("Your power is", result)

    case "Multiplication":
        result = x * y
        print("Your multiplication is", result)

    case "Division":
        if y == 0:
            print("You can't divide by zero")
        else:
            result = x / y
            print("Your division is", result)

    case "sin":
        result = math.sin(math.radians(x))
        print("sin(x) =", result)

    case "cos":
        result = math.cos(math.radians(x))
        print("cos(x) =", result)

    case _:
        print("Invalid operation")