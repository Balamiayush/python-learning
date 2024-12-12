
# Here are 10 practice problems related to Python functions, ranging from beginner to intermediate levels:
# 1. Greet User
def greet_user(name):
    """
    Greet the user with a personalized message.

    Parameters:
    name (str): The name of the user to greet.

    Returns:
    None
    """
    print(f"Hello, {name}!")

# Prompt the user to enter their name
name = input("Enter your name: ")

# Call the function to greet the user
greet_user(name)

# Print the docstring of the greet_user function
print(greet_user.__doc__)
