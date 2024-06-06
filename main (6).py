def calculate_exam_points():
  # Get user input for student's last name, midterm exam score, and final exam score
  last_name = input("Enter the student's last name: ")
  midterm_score = float(input("Enter the midterm exam score: "))
  final_exam_score = float(input("Enter the final exam score: "))

  # Calculate the total exam points
  total_exam_points = (0.4 * midterm_score) + (0.6 * final_exam_score)

  # Display the results
  print(f"\nStudent Last Name: {last_name}")
  print(f"Total Exam Points: {total_exam_points:.2f}")

# Run the function
calculate_exam_points()