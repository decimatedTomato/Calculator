# Select first number
def input_a():
    a = input("First number:\n")
    try:
        return float(a)
    except:
        if a == "die":
            exit()
        print(a + " is not a number. Enter a number next time please!")
        input_a()


# Select operation
def input_op():
    return input("Operation:\n")


def input_b():
    b = input("Second number:\n")
    try:
        return float(b)
    except:
        if b == "die":
            exit()
        print(b + " is not a number. Enter a number next time please!")
        input_b()


# Select second number
def compute(a, operation, b):
    if operation == "add" or operation == "plus" or operation == '+':
        return a + b
    elif operation == "subtract" or operation == "minus" or operation == '-':
        return a - b
    elif operation == "multiply" or operation == "times" or operation == 'x' or operation == '*':
        return a * b
    elif operation == "divide" or operation == "over" or operation == '/':
        return a / b
    else:
        raise


try:
    print(compute(input_a(), input_op(), input_b()))
except:
    print("you appear to have made a fucky-wucky!")
