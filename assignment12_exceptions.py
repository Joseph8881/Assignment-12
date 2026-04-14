# assignment12_exceptions.py
# IST105 Assignment 12
# Handling Exceptions and Testing Python Code

print("Debug: Program Started")

numbers = []

# Ask user to input five integers
for i in range(5):
    while True:
        try:
            print(f"Debug: Asking for number {i+1}")
            num = int(input(f"Enter integer {i+1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Error: Invalid input! Please enter integers only.")

print("Debug: Numbers entered:", numbers)

try:
    # Calculate sum
    print("Debug: Calculating sum")
    total = sum(numbers)
    print("Sum:", total)

    # Force ZeroDivisionError if total is zero (for testing requirement)
    print("Debug: Calculating average")
    if total == 0:
        raise ZeroDivisionError("Total is zero, cannot divide")

    average = total / len(numbers)
    print("Average:", average)

except ZeroDivisionError:
    print("Error: Division by zero occurred while calculating average")

except Exception as e:
    print("Unexpected error:", e)

# Count positive numbers
print("Debug: Counting positive numbers")
positive_count = sum(1 for n in numbers if n > 0)
print("Positive Numbers Count:", positive_count)

# Even/Odd using bitwise operator
print("\nEven/Odd Results:")
for n in numbers:
    if n & 1:
        print(n, "is Odd")
    else:
        print(n, "is Even")

# Numbers greater than 10
print("\nDebug: Finding numbers greater than 10")
greater_than_10 = sorted([n for n in numbers if n > 10])

print("Numbers greater than 10 (Sorted):")
print(greater_than_10)

print("Debug: Program Completed Successfully")
