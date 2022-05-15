def addtiton(x, y):
    print(x + y)


def substraction(x, y):
    print(x - y)


def multiplication(x, y):
    print(x * y)


def division(x, y):
    if y == 0:
        print("second number cannot be 0")
        main()
    else:
        print(x / y)


def process(data1, data2):
    function1 = str.upper(input("what to do want to do the numbers ? "))
    if function1 == "ADD":
        addtiton(data1, data2)
    elif function1 == "MULTIPLY":
        multiplication(data1, data2)
    elif function1 == "SUBSTRACT":
        substraction(data1, data2)
    elif function1 == "DIVIDE":
        division(data1, data2)
    else:
        print("please make correct choice:")
        process(data1, data2)


def main():
    print('''
    welcome to my simple calculator  <3 
    Please enter two numbers to calculate
    And then select the type of calculation for you choice
    ----> "Add" for Addition
    ----> "Substract" for Substraction
    ----> "Multiply" for Multiplication
    ----> "Divide" for Division
    ''')
    data1 = int(input("Please enter ur 1st number: "))
    data2 = int(input("Please enter ur 2nd number: "))
    process(data1, data2)


main()
