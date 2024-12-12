def is_prime(n):
    """
    Check if a number is prime.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(n**0.5) + 1):  # Check divisors up to √n
        if n % i == 0:
            return False  # If divisible, not prime
    return True  # If no divisors found, it's prime


# Get input from the user
num = int(input("Enter a number to check if it's prime: "))

# Call the function and display the result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
