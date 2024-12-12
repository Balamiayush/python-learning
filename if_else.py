# A simple program to determine the type of weather
temperature = int(input("Enter the temperature: "))

if temperature > 30:
    print("It's a hot day! ☀️")
elif temperature > 20:
    print("It's a nice day! 🌤️")
else:
    print("It's a bit chilly! ❄️")
