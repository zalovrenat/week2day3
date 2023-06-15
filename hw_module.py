def area(length, width, levels, units):
    total_area = length*width*levels
    print(f"The total square {units}-age of the house is {total_area} {units}s^2")

from math import pi

def circ(radius, units):
    circumference = 2*pi*radius
    print(f"The circumference of the circle is {circumference} {units}")
