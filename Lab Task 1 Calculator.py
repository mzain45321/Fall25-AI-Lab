import re
print("My Calculator")
print("Enter 'exit' to quit/n ")
while True:
    expression = input("Enter expression: ")
    if expression.lower() == 'exit':
        break
    expression = expression.replace("×", "*").replace("÷", "/")
    expression = re.sub(r'(\d)(\()', r'\1*(',expression)
    expression = expression.replace(")(", ")*(")
    
    try:
        result = eval(expression)
        print("Rrsult: ", result)
    except Exception as e:
        print("Invalid Expression")