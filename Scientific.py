import math

def calculate(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    elif operator == '%':
        return operand1 % operand2
    elif operator == 'sqrt':
        return math.sqrt(operand1)
    elif operator == 'exp':
        return math.pow(operand1, operand2)
    elif operator == 'sin':
        return math.sin(operand1)
    elif operator == 'cos':
        return math.cos(operand1)
    elif operator == 'tan':
        return math.tan(operand1)
    elif operator == 'rad_to_deg':
        return math.degrees(operand1)
    elif operator == 'deg_to_rad':
        return math.radians(operand1)

def main():
    while True:
        operator = input("Enter an operator (+, -, *, /, %, sqrt, exp, sin, cos, tan, rad_to_deg, deg_to_rad): ")
        if operator == 'exit':
            break
        operand1 = float(input("Enter the first operand: "))
        if operator in ['+', '-', '*', '/', '%', 'exp']:
            operand2 = float(input("Enter the second operand: "))
        else:
            operand2 = None

        result = calculate(operator,operand1,operand2)
        print (result)
main()
