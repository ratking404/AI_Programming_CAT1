from math import pi  # Import pi from the math library

def area_of_circle(radius):
    # Step 1: Validate radius
    if radius <= 0:
        return "Invalid input – radius must be greater than 0."
    
    # Step 2: Calculate area
    area = pi * radius ** 2
    
    # Step 3: Return the area rounded to 2 decimal places
    return round(area, 2)

# --- Main program ---
# Ask the user to enter the radius
radius = float(input("Enter the radius of the circle: "))

# Call the function and print the result-5
result = area_of_circle(radius)
print("The area of the circle is:", result)
