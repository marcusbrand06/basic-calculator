operator = input("What do you want to do? Add, Subtract, Divide or Multiply? ")
num1 = float(input("What's the first number? "))
num2 = float(input("What's the second number? "))

if operator == "Add":
    print(num1 + num2)
elif operator == "Subtract":
    print(num1 - num2)
elif operator == "Divide":
    print(num1 / num2)
elif operator == "Multiply":
    print(num1 * num2)