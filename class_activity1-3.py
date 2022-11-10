import math

def compute_area(r):
    return math.pi * r * r 

radius = float(input("Please enter a radius: "))

print(f"The area is: + {compute_area(radius)}")