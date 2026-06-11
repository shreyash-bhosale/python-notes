# ================================
# EXCEPTION HANDLING IN PYTHON
# ================================

# Errors vs Exceptions
# Errors → caused by incorrect syntax (can't be handled)
# Exceptions → runtime issues (can be handled)

# Example of handling an exception

try:
    # Risky code (may cause an error)
    num = int(input("Enter a number: "))
    result = 10 / num

except ZeroDivisionError:
    # Runs if user enters 0
    print("Error: Division by zero is not allowed.")

except ValueError:
    # Runs if user enters non-number
    print("Error: Please enter a valid number.")

else:
    # Runs only if no exception occurs
    print("Success! Result =", result)

finally:
    # Always executes
    print("Execution completed.\n")


# Keywords Summary:
# try     → contains risky code
# except  → handles specific errors
# else    → runs if no error happens
# finally → always runs


# ================================
# FILE HANDLING IN PYTHON
# ================================

# File Modes:
# 'r' → Read (file must exist)
# 'w' → Write (overwrites file or creates new)
# 'a' → Append (adds content at end)
# 'x' → Create (fails if file already exists)

# -------------------------------
# WRITING TO A FILE
# -------------------------------
with open("notes.txt", "w") as file:
    file.write("Hello from Python!\n")
    file.write("This is file handling.\n")

print("Data written to file.\n")

# -------------------------------
# READING FROM A FILE
# -------------------------------
with open("notes.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

# -------------------------------
# APPENDING TO A FILE
# -------------------------------
with open("notes.txt", "a") as file:
    file.write("This line was added later.\n")

print("New data appended.\n")

# -------------------------------
# IMPORTANT NOTE
# -------------------------------
# Using 'with open(...)' automatically closes the file
# even if an error occurs — this is best practice!