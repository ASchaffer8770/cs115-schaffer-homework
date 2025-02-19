"""
Alex Schaffer
02/19/2025
Python Introduction
Description:
  Basic Arithmetic Program accepting two inputs from user on CLI
"""
def main():
  try:
    #prompting user for the input of the two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    #preforming the basic arithmetic
    print(f"Addition: {num1} + {num2} = {num1 + num2}")
    print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
    print(f"Multiplication: {num1} * {num2} = {num1 * num2}")

    """
    We do some basic input checking for the number 0. Dividing
    by zero is not possible. If num2 is = 0 we print a seperate
    statement.
    """
    if num2 != 0:
      print(f"Division: {num1} / {num2} = {num1 / num2}")
    else:
      print(f"Division by zero isn't possible, even for python!")

  #Checking for just number inputs if input != float type throw error
  except ValueError:
    print(f"Please only enter numerical values!")

#Run the main function
if __name__ == "__main__":
  main()