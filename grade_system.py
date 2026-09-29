def grade_system():
    try:
        # Ask the user to enter a mark
        mark = float(input("Enter a mark (0-100): "))

        # Validate range
        if mark < 0 or mark > 100:
            print("Invalid mark. Please enter a value between 0 and 100.")
        elif mark >= 90:
            print("Grade: A")
        elif mark >= 80:
            print("Grade: B")
        elif mark >= 70:
            print("Grade: C")
        elif mark >= 60:
            print("Grade: D")
        else:
            print("Grade: F")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

grade_system()