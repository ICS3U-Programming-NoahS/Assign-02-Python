#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Oct 11th, 2023
# This program calculates and displays
# the volume and surface area of a
# cube with the proper unit of measurement.
import math


def main():
    # Get the side length
    side_length = float(input("Enter the side length: "))

    # Check if the side length is greater than 0
    if side_length <= 0:
        print("Please enter a number greater than 0!")

    # Get the unit of measurement
    unit = input("Enter the unit of measurement: ")

    # Calculate the volume and surface area
    volume = side_length * side_length * side_length
    surface_area = side_length * side_length * 6

    # Display the volume and the surface area back to the user, with proper units
    print("")
    print("The volume is {:.2f}{}^3".format(volume, unit))
    print("The surface_area is {:.2f}{}^2".format(surface_area, unit))


if __name__ == "__main__":
    main()
