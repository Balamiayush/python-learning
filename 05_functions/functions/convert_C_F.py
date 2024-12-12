def conver_C_F(n):
    """
    Convert Celsius to Fahrenheit.
    """
    fahrenheit = (n * 9/5) + 32
    return fahrenheit

# Get input from the user

celsius = float(input("Enter the temperature in Celsius: "))

# Call the function

fahrenheit = conver_C_F(celsius)

# Print the result

print(f"{celsius}°C is equal to {fahrenheit}°F.")

print(conver_C_F.__doc__)

# Test the function