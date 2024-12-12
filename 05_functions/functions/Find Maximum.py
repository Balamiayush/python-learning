# 2. Find Maximum
# Write a function find_max(a, b, c) that takes three numbers as input and returns the largest among them.

def find_max(a, b, c):
    """
    Returns the maximum of three numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.
    c (int): The third number.

    Returns:
    int: The largest of the three numbers.
    """
    return max(a, b, c)

# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Call the function
result = find_max(num1, num2, num3)

# Print the result
print(f"{result}: MAX among three")
