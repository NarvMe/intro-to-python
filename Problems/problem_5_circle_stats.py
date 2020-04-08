"""
Fill out the functions to calculate the area and circumference of a circle.
Print the result to the user.
"""
from math import pi

def area(r):
    return  pi * r**2




def circumference(r):
    return 2*pi*r



radius = float(input("Circle radius: "))

print(f'Area: {area(radius)}')  # <-- Call the area function and print the result
print('Circumference: {}'.format(circumference(radius)))  # <-- Call the circumference function and print
