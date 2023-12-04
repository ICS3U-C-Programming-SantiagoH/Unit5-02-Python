#!/usr/bin/env python3

# Created by: Santiago Hewett
# Created on: Nov 28, 2023
# This program will ask the user for the base and
# height of a triangle and display the area
# using multiple functions


def calc_area_triangle(base, height):
    # Calculate area
    area = (base * height) / 2
    # Display area to the user
    print("\n{:.2f}cm x {:.2f}cm = {:.2f}cm^2".format(base, height, area))


def main():
    # Get base and height from the user and display a message about the program
    print("This program will ask the user for the base and ")
    print("height of a triangle and display the area in cm.")

    user_base_str = input("Please enter the base of the triangle (cm): ")
    user_height_str = input("Please enter the height of the triangle (cm): ")

    try:
        # Convert base as a string to float
        user_base_float = float(user_base_str)
        # Convert height as a string to float
        user_height_float = float(user_height_str)

        # Call the calc_area_triangle function
        calc_area_triangle(user_base_float, user_height_float)

    except ValueError:
        # Message for invalid user number
        print(
            "\n{} and {} are not valid base and height.".format(
                user_base_str, user_height_str
            )
        )


if __name__ == "__main__":
    main()
