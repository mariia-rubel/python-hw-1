import sys
from turtle import left


if len(sys.argv) !=4:
    print('Arg len should be 4')
    sys.exit()



left_operand = sys.argv[1]
right_operand = sys.argc[3]

operation = sys.argv[2]

allowed_operations = ['+', '-', '/', '*']

if operation not in allowed_operations:
     print('Maximum arg len is 4')
     
try:
    left_operand = int(left_operand)
    right_operand = int(left_operand)
except ValueError:
    print('Left and Right operands must be int')
    sys.exit()

if operation == '/' and right_operand == 0:
    print ('Division by zero is not allowed')
    sys.exit()

match operation:
    case '*':
        print(left_operand*right_operand)
    case '+':
        print(left_operand+right_operand)
    case '-':
        print(left_operand-right_operand)
    case '/':
        print(left_operand/right_operand)
sys.exit()


# print(sys.argv[1])
# print(sys.argv[2])
# print(sys.argv[3])