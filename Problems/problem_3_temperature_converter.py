"""
Given a temperature in Fahrenheit, return the temperature in Celsius
"""
# Ask for a temperature in Fahrenheit
temp_fahrenheit = float(input("Give me Fahrenheit"))
# Calculate it in Celsius
temp_celsius = (temp_fahrenheit-32) * 5/9

# Tell the user what it is
print("{} Fahrenheit are {} Celsius".format(temp_fahrenheit,temp_celsius))

