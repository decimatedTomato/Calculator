# Updates to the calculator
# I don't know what order to put the code in
operators = [
    ["add", "plus", "+"],  # a + b
    ["subtract", "minus", "-"],  # a - b
    ["multiply", "times", "x", "*"],  # a * b
    ["divide", "by", "over", "/"],  # a / b
    ["remainder", "modulus", "%"],  # a % b
    ["to the power of", "to the", "exponent", "^", "**"]  # a * a * a * ... (b times)
]
ans = None


# Select first number
def input_a():
    while True:
        a = input("First number:\n")
        if a == "exit":
            exit()
        elif (a == "ans" or a == "answer") and (ans is not None):
            return float(ans)
        try:
            return float(a)
        except ValueError:
            print(a + " is not a number. Enter a number next time please!")


# Select operation
def input_op():
    while True:
        op = input("Operation:\n")
        if op == "exit":
            exit()
        elif any(op in sublist for sublist in operators):
            return op
        elif op == "help":
            for operator in range(0, len(operators)):
                print(operators[operator])
            print("\n")
        else:
            print(op + " is not a supported operation. Type help for a full list of supported operations\n")


# Select second number
def input_b():
    while True:
        b = input("Second number:\n")
        if b == "exit":
            exit()
        elif (b == "ans" or b == "answer") and (ans is not None):
            return float(ans)
        try:
            return float(b)
        except ValueError:
            print(b + " is not a number. Enter a number next time please!")
            input_b()


# return the computation or raise a generic error
def compute(a, operation, b):
    if operation in operators[0]:
        return [a, operation, b, str(a + b)]
    elif operation in operators[1]:
        return [a, operation, b, str(a - b)]
    elif operation in operators[2]:
        return [a, operation, b, str(a * b)]
    elif operation in operators[3]:
        return [a, operation, b, str(a / b)]
    elif operation in operators[4]:
        return [a, operation, b, str(a % b)]
    elif operation in operators[5]:
        return [a, operation, b, str(a ** b)]
    else:
        raise


while True:
    try:
        result = compute(input_a(), input_op(), input_b())
        ans = result[3]
        print(str(result[0]) + " " + result[1] + " " + str(result[2]) + " = " + ans + "\n")
    except ValueError:
        print("you appear to have made a fucky-wucky! Somehow?")
        break
