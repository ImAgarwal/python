
 
        # input from user
number_input = float(input("Enter a number: "))
        # Check if the number is less than zero
try:
        if number_input < 0:
            raise ValueError("The number cannot be less than zero.")
        # Print the number if it's zero or greater
        print(f"You entered: {number_input}")
    
except ValueError as ve:
        # Handle the ValueError exception
        print(f"Error: {ve}")

# Call the main function

