def sum_of_list(num):
    """
    Calculate the sum of all numbers in a list.

    Parameters:
    num (list): A list of numbers.

    Returns:
    float: The sum of the numbers in the list.
    """
    return sum(num)

# Input: Get numbers as a space-separated string
numbers = input("Enter the numbers separated by spaces: ")

# Convert the string to a list of floats
num = [float(i) for i in numbers.split()]

# Call the function to calculate the sum
result = sum_of_list(num)

# Print the result
print(f"The sum of the numbers in the list is: {result}")
