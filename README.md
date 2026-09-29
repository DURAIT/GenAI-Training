# Grade System Application

## Overview

This Python program allows users to enter a student mark between **0 and 100** and automatically assigns a corresponding letter grade based on predefined grading criteria.

The application includes:

- User input validation
- Grade calculation
- Exception handling for invalid inputs
- Range validation to ensure marks are between 0 and 100

---

## Features

✅ Accepts numeric marks from 0 to 100

✅ Assigns grades based on score ranges

✅ Handles non-numeric input gracefully

✅ Validates acceptable mark range

✅ Displays meaningful error messages

---

## Grade Criteria

| Mark Range | Grade |
|------------|--------|
| 90 - 100 | A |
| 80 - 89 | B |
| 70 - 79 | C |
| 60 - 69 | D |
| 0 - 59 | F |

---

## Prerequisites

- Python 3.x installed on your system

Verify Python installation:

```bash
python --version
```

or

```bash
python3 --version
```

---

## How to Run

### 1. Save the code

Create a file named:

```text
grade_system.py
```

Paste the Python code into the file.

### 2. Execute the program

```bash
python grade_system.py
```

or

```bash
python3 grade_system.py
```

---

## Sample Execution

### Valid Input

```text
Enter a mark (0-100): 85
Grade: B
```

### Invalid Range

```text
Enter a mark (0-100): 120
Invalid mark. Please enter a value between 0 and 100.
```

### Non-Numeric Input

```text
Enter a mark (0-100): abc
Invalid input. Please enter a numeric value.
```

---

## Code Structure

### Function

#### `grade_system()`

Responsible for:

1. Prompting the user for a mark.
2. Converting user input to a numeric value.
3. Validating the mark range.
4. Determining and displaying the appropriate grade.
5. Handling invalid and unexpected errors.

---

## Exception Handling

### ValueError

Occurs when the user enters a non-numeric value.

Example:

```text
abc
```

Output:

```text
Invalid input. Please enter a numeric value.
```

### Generic Exception

Captures any unexpected runtime errors and displays the error message.

```python
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

---

## Example Grading Logic

```python
if mark >= 90:
    print("Grade: A")
elif mark >= 80:
    print("Grade: B")
elif mark >= 70:
    print("Grade: C")
elif mark >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

---

## Future Enhancements

Possible improvements include:

- Support for multiple students
- Percentage and GPA calculations
- Grade reporting to a file
- Graphical User Interface (GUI)
- Unit testing using `pytest`
- Customizable grade boundaries

---

## Author

Created as a simple Python learning project demonstrating:

- Conditional statements (`if-elif-else`)
- Functions
- Input validation
- Exception handling
- User interaction

---

## License

This project is free to use for educational and learning purposes.
