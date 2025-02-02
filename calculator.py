def plus():
  print("ADDITION \n")
  while True:
    num1 = input("enter first number: ")
    if num1.isdigit():
      break
    else:
      print("please enter a valid number")

  while True:
    num2 = input("enter second number: ")
    if num2.isdigit():
      break
    else:
      print("please enter a valid number")
  print(f"\n result is {int(num1) + int(num2)}")
    

def minus():
  print("MINUS\n")
  while True:
    num1 = input(" enter first number: ")
    if num1.isdigit():
      break
    else:
      print("please enter a valid number")
  while True:
    num2 = input(" enter first number :")
    if num2.isdigit():
      break
    else:
      print("please enter a valid number")
  print(f"\n result is {int(num1) - int(num2)}")


def multiply():
  print("MULTIFICATIONS\n")
  while True:
    num1 = input("Enter first number :")
    if num1.isdigit():
      break
    else:
      print("please enter a valid number!!!")
  while True:
    num2 = input("Enter second number :")
    if num2.isdigit():
      break
    else:
      print("please enter a valid number!!!")
  print(f"\n result is {int(num1) * int(num2)}")

def division():
  print("DIVISION\n")
  while True:
    num1 = input("Enter first number :")
    if num1.isdigit():
      break
    else:
      print("please enter a valid number!!!")
  while True:
    num2 = input("enter second number :")
    if num2.isdigit():
      break
    else:
      print("please enter a valid number !!!")
  print(f"result is {int(num1) / int(num2)}")

def advance():
  print("comming soon...")
  pass

while True:
  print("Welcome to the calculator\n")
  print("1. Addition")
  print("2. Subtraction")
  print("3. multification")
  print("4. division")
  print("5. advance math")
  print("6. quit")

  choice = input("Enter your action (1-6): ")

  if choice.isdigit():
      num_choice = int(choice)

      if 0 < num_choice < 7:
          if num_choice == 1:
              plus()
          elif num_choice == 2:
              minus()
          elif num_choice == 3:
              multiply()
          elif num_choice == 4:
              division()
          elif num_choice == 5:
              advance()
          elif num_choice == 6:
              print("Thank you for using the calculator")
              break
      else:
          print("Invalid choice! Please enter a number between 1 and 6.\n")
  else:
      print("Invalid input! Please enter a digit.\n")
