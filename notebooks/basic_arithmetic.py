# Basic Arithmetic Operations in Python
# This file demonstrates fundamental arithmetic operations with examples

# Addition: Adds two numbers
add_result = 5 + 3  # Result: 8
print(f"Addition: 5 + 3 = {add_result}")

# Subtraction: Subtracts the right operand from the left
sub_result = 10 - 4  # Result: 6
print(f"Subtraction: 10 - 4 = {sub_result}")

# Multiplication: Multiplies two numbers
mul_result = 6 * 7  # Result: 42
print(f"Multiplication: 6 * 7 = {mul_result}")

# Division: Divides the left operand by the right
# Returns a floating-point number
div_result = 15 / 3  # Result: 5.0
print(f"Division: 15 / 3 = {div_result}")

# Floor Division: Divides and returns the largest integer less than or equal to the result
floor_div_result = 17 // 3  # Result: 5 (not 5.666...)
print(f"Floor Division: 17 // 3 = {floor_div_result}")

# Modulus: Returns the remainder of division
mod_result = 17 % 3  # Result: 2 (remainder of 17 divided by 3)
print(f"Modulus: 17 % 3 = {mod_result}")

# Exponentiation: Raises the left operand to the power of the right
exp_result = 2 ** 3  # Result: 8 (2^3)
print(f"Exponentiation: 2 ** 3 = {exp_result}")

# Operator Precedence Example
# Parentheses have the highest precedence
precedence_result = (5 + 3) * 2  # Result: 16 (8 * 2)
print(f"Operator Precedence: (5 + 3) * 2 = {precedence_result}")

# Combining Operations
combined_result = 10 + 5 * 2 - 8 / 4  # Follows PEMDAS/BODMAS rules
print(f"Combined Operations: 10 + 5 * 2 - 8 / 4 = {combined_result}")

# Working with Variables
x = 10
y = 3
z = x + y * 2  # z = 10 + (3 * 2) = 16
print(f"Working with Variables: x + y * 2 = {z} (where x={x}, y={y})")