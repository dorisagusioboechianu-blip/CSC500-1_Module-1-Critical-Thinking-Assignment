# Program to find multiplication and division of two numbers

# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform multiplication
mul_result = num1 * num2

# Perform division (handle divide-by-zero safely)
if num2 != 0:
    div_result = num1 / num2
else:
    div_result = "Undefined (cannot divide by zero)"

# Display the results
print("The product of", num1, "and", num2, "is:", mul_result)
print("The division of", num1, "by", num2, "is:", div_result)
