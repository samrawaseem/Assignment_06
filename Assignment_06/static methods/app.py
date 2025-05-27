class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Using the static method without creating an instance
temp_c = 25
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is {temp_f}°F")

# #- The code defines a class called TemperatureConverter.
# - Inside the class, there is a static method named celsius_to_fahrenheit.
# - A static method means you can use it without making an object of the class.
# - The method takes a Celsius temperature (c) and converts it to Fahrenheit using the formula: (c * 9/5) + 32.
# - The code sets temp_c to 25 (25°C).
# - It calls the static method to convert 25°C to Fahrenheit and stores the result in temp_f.
# - Finally, it prints out "25°C is 77.0°F"