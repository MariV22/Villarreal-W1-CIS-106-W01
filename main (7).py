def split_payment():
  # Get user input for the total amount received
  total_amount = float(input("Enter the total amount received: "))

  # Calculate the amount each person will receive
  amount_per_person = total_amount / 3

  # Display the results
  print(f"\nTotal Amount Received: ${total_amount:.2f}")
  print(f"Amount Each Person Receives: ${amount_per_person:.2f}")

# Run the function
split_payment()
