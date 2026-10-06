### Main Exception Handling Keywords.

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative")

except ValueError as e:
    print("Error:", e)

else:
    print("Your age is:", age)

finally:
    print("Program finished")