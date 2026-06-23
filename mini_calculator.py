# -----------------------------------
# Mini Calculator
# Author: Chitrakch Kushwaha
# Language: Python
# Description:
# A menu-driven calculator with
# exception handling and decimal support.
# -----------------------------------
print("================Mini Calculator================")

while True:
  def numbers():
     num1 = float(input("Enter first number: "))
     num2 = float(input("Enter second number: "))
     return num1, num2
#Main Menu
  print("================MENU================")
  print("1. Addition ")
  print("2. Subtraction ")
  print("3. Multiplication ")
  print("4. Division ")
  print("5. Exit ")
  choice = input("Enter your choice: ")
#Addition
  if choice == "1":
     while True:
        try:
           num1, num2 = numbers()
           result = num1 + num2
           print(f"Sum of {num1} and {num2} is {result}")
           break
        except ValueError:
            print("Invalid input. Please enter a number.")
#Subtraction
  elif choice == "2":
        while True:
          try:
            num1, num2 = numbers()
            result = num1 - num2
            print(f"The difference between {num1} and {num2} is {result}")
            break
          except ValueError:
            print("Invalid input. Please enter a number.")
#Multiplication
  elif choice == "3":
        while True:
            try:
             num1, num2 = numbers()
             result = num1 * num2
             print(f"The product of {num1} and {num2} is {result}")
             break
            except ValueError:
             print("Invalid input. Please enter a number.")
#Division
  elif choice == "4":
        while True:
         try:
          num1, num2 = numbers()

          result = num1 / num2
          print(f"The quotient of {num1} and {num2} is {result}")
          break
         except ValueError:
            print("Invalid input. Please enter a number.")
         except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
#Exit
  elif choice == "5":
    print("Thank you for using Mini Calculator! Goodbye! 👋 ")
    break
  else:
    print("Invalid choice. Please try again.Enter a number 1-5. ")  
