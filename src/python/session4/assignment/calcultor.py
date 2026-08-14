def calc(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

def main():
    contin = True
    while contin==True:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        result = calc(num1, num2, operator)
        print("Result: of", num1, operator, num2, "is", result)
        continue_calculation = input("Do you want to perform another calculation? (yes/no): ").lower() == 'yes'
        if not continue_calculation:
            contin = False

if __name__ == "__main__":
    main()