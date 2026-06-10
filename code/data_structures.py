
"""
DATA STRUCTURES IN PYTHON

What are Data Structures?
Data structures are used to store multiple values in a single variable.
Python provides 4 built-in data structures:

Structure     Ordered   Mutable   Duplicates   Access By
--------------------------------------------------------
List          Yes       Yes       Yes          Index
Tuple         Yes       No        Yes          Index
Set           No        Yes       No           Methods
Dictionary    Yes       Yes       Keys: No     Key
"""

"""
========================================================
LIST
========================================================

Lists are ordered, changeable, and allow duplicate values.

# Creating a list
fruits = ["apple", "banana", "mango"]

# Accessing elements
print(fruits[0])    # apple
print(fruits[-1])   # mango (last element)
print(fruits[0:2])  # ['apple', 'banana']

# Modifying list (lists are mutable)
fruits[1] = "grape"

--------------------------------------------------------
Common List Methods

lst = [3, 1, 4, 1, 5]

lst.append(9)       # Add element at end
lst.insert(0, 0)    # Insert at specific index
lst.remove(1)       # Remove first occurrence of 1
lst.pop()           # Remove last element
lst.sort()          # Sort list
lst.reverse()       # Reverse list
print(len(lst))     # Length of list
"""
"""
--------------------------------------------------------
List Questions
"""
# Q1: Separate positive and negative numbers
arr = [3, -1, 4, -5, 9]
pos = []
neg = []

for i in arr:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)

print("Positive:", pos)
print("Negative:", neg)

# Q2: Find mean (average)
arr = [10, 20, 30, 40]
mean = sum(arr) / len(arr)
print("Mean =", mean)

# Q3: Find greatest element and index
arr = [4, 8, 2, 9, 1]
max_val = max(arr)
print("Greatest =", max_val, "at index", arr.index(max_val))

# Q4: Find second greatest element
arr = [4, 8, 2, 9, 1]
arr_sorted = sorted(arr)
print("Second greatest =", arr_sorted[-2])

# Q5: Check if list is sorted
arr = [1, 3, 5, 7]
if arr == sorted(arr):
    print("List is sorted")
else:
    print("Not sorted")
"""
========================================================
TUPLE
========================================================

Tuples are like lists but immutable (cannot be changed).

days = ("Mon", "Tue", "Wed")

print(days[0])   # Mon

# days[0] = "X"  ❌ Error (tuples cannot be modified)

--------------------------------------------------------
Tuple Methods

t = (1, 2, 3, 2, 1)

print(t.index(2))   # First occurrence index
print(t.count(2))   # Count occurrences

========================================================
SET
========================================================

Sets store only unique values and are unordered.

s = {1, 2, 2, 3, 3}
print(s)   # {1, 2, 3}

--------------------------------------------------------
Set Operations

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # Union
print(a & b)   # Intersection
print(a - b)   # Difference
print(a ^ b)   # Symmetric difference

========================================================
DICTIONARY
========================================================

Dictionaries store data in key-value pairs.

person = {"name": "Akarsh", "age": 20, "city": "Indore"}

# Access value
print(person["name"])

# Update value
person["age"] = 21

# Add new key-value
person["course"] = "Python"

# Delete key
del person["city"]

# Traverse dictionary
for key, val in person.items():
    print(key, "→", val)
"""
"""
--------------------------------------------------------
Dictionary Questions
"""
# Q1: Merge two dictionaries
d1 = {"a": 1}
d2 = {"b": 2}
merged = {**d1, **d2}
print(merged)

# Q2: Sum of values
d = {"a": 10, "b": 20, "c": 30}
print("Sum =", sum(d.values()))

# Q3: Frequency count using dictionary
arr = ["a", "b", "a", "c", "b", "a"]
freq = {}

for item in arr:
    freq[item] = freq.get(item, 0) + 1

print(freq)

# Q4: Combine dicts with addition for common keys
d1 = {"a": 5, "b": 3}
d2 = {"b": 4, "c": 2}

result = {}

for key in d1:
    result[key] = d1[key]

for key in d2:
    if key in result:
        result[key] += d2[key]
    else:
        result[key] = d2[key]

print(result)
"""
========================================================
SUMMARY

- List → Ordered, mutable, allows duplicates
- Tuple → Ordered, immutable
- Set → Unordered, unique values only
- Dictionary → Key-value pairs for fast access

These are the foundation of Python and are heavily used in real-world coding.
"""

