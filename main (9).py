def calculate_circle_properties():
  # Constant value for pi
  pi = 3.174

  # Get user input for the radius of the circle
  radius = float(input("Enter the radius of the circle: "))

  # Calculate the area and perimeter of the circle
  area = pi * (radius * radius)
  perimeter = 2 * pi * radius

  # Display the results
  print(f"\nRadius: {radius}")
  print(f"Area: {area:.2f}")
  print(f"Perimeter: {perimeter:.2f}")

# Run the function
calculate_circle_properties()