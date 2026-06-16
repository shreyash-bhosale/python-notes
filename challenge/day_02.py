# 🚀 CHALLENGE DAY 02 - Lists, Tuples, Dictionaries & Sets


# ============================================================
# 📋 LISTS IN PYTHON
# ============================================================

# A list is a built-in data type that stores a collection of values
# Lists are ORDERED and MUTABLE (can be changed after creation)
# Lists can store elements of different types (int, float, str, etc.)

marks = [87, 64, 33, 95, 76]           # list of integers
student = ["Karan", 85, "Delhi"]        # list with mixed types (str, int, str)

print(marks)     # prints entire list → [87, 64, 33, 95, 76]
print(student)   # prints entire list → ['Karan', 85, 'Delhi']


# ACCESSING LIST ELEMENTS (Indexing)
# Positive index → left to right (starts at 0)
# Negative index → right to left (starts at -1)

print(marks[0])    # first element → 87
print(marks[1])    # second element → 64
print(marks[-1])   # last element → 76 (negative indexing)
print(marks[-2])   # second from last → 95


# MODIFYING LIST ELEMENTS (Lists are mutable!)

student[0] = "Arjun"    # changing first element from "Karan" to "Arjun"
print(student)           # → ['Arjun', 85, 'Delhi']


# LENGTH OF A LIST

print(len(marks))    # returns total number of elements → 5
print(len(student))  # → 3


# ============================================================
# ✂️ LIST SLICING
# ============================================================

# Syntax: list_name[starting_idx : ending_idx]
# Ending index is NOT included in the result
# Similar to String Slicing!

marks = [87, 64, 33, 95, 76]

print(marks[1:4])    # index 1 to 3 → [64, 33, 95]
print(marks[:4])     # same as marks[0:4] → [87, 64, 33, 95]
print(marks[1:])     # same as marks[1:len(marks)] → [64, 33, 95, 76]
print(marks[-3:-1])  # negative slicing → [33, 95]
print(marks[:])      # full list copy → [87, 64, 33, 95, 76]

# Slicing with step: list[start:end:step]
print(marks[::2])    # every 2nd element → [87, 33, 76]
print(marks[::-1])   # reverse the list using slicing → [76, 95, 33, 64, 87]


# ============================================================
# 🔧 LIST METHODS
# ============================================================

lst = [2, 1, 3]

# append(el) — adds ONE element at the END of the list
lst.append(4)
print(lst)   # → [2, 1, 3, 4]

# insert(idx, el) — inserts element at a SPECIFIC index
lst.insert(1, 99)    # insert 99 at index 1, shift rest right
print(lst)           # → [2, 99, 1, 3, 4]

# sort() — sorts list in ASCENDING order (modifies original list)
lst2 = [5, 2, 8, 1, 9]
lst2.sort()
print(lst2)   # → [1, 2, 5, 8, 9]

# sort(reverse=True) — sorts list in DESCENDING order
lst2.sort(reverse=True)
print(lst2)   # → [9, 8, 5, 2, 1]

# reverse() — REVERSES the order (not sorted, just flipped)
lst3 = [2, 1, 3]
lst3.reverse()
print(lst3)   # → [3, 1, 2]

# remove(el) — removes the FIRST occurrence of the given element
lst4 = [2, 1, 3, 1]
lst4.remove(1)    # removes first '1' found (at index 1)
print(lst4)       # → [2, 3, 1]  (second '1' at the end stays)

# pop(idx) — removes and RETURNS element at given index
lst5 = [10, 20, 30, 40]
lst5.pop(2)              # removes element at index 2 (value 30)
print(lst5)              # → [10, 20, 40]

removed = lst5.pop(0)    # removes first element and stores it
print(removed)           # → 10
print(lst5)              # → [20, 40]

# copy() — creates an INDEPENDENT copy of the list
original = [1, 2, 3]
copied = original.copy()    # separate copy in memory
copied[0] = 99              # modifying copy does NOT affect original
print(original)             # → [1, 2, 3]  ← unchanged
print(copied)               # → [99, 2, 3]

# NOTE: Why not just do `copied = original`?
# That would make BOTH point to the same list (not a real copy)
wrong_copy = original        # same memory reference
wrong_copy[0] = 999          # this changes original too!
print(original)              # → [999, 2, 3]  ← changed!


# ============================================================
# 📦 TUPLES IN PYTHON
# ============================================================

# A tuple is a built-in data type that creates IMMUTABLE sequences
# Tuples are ORDERED but CANNOT be modified after creation
# Tuples use () instead of []
# Use tuples when data should not change (e.g. days of week, coordinates)

tup = (87, 64, 33, 95, 76)    # tuple of integers

print(tup)       # → (87, 64, 33, 95, 76)
print(tup[0])    # → 87 (indexing works the same as lists)
print(tup[-1])   # → 76

# tup[0] = 43   # ❌ TypeError! Tuples are immutable — NOT allowed

# Different ways to create tuples
tup1 = ()           # empty tuple
tup2 = (1,)         # single-element tuple — trailing comma is REQUIRED!
tup3 = (1, 2, 3)    # normal tuple

print(tup1)   # → ()
print(tup2)   # → (1,)
print(tup3)   # → (1, 2, 3)

# ⚠️ IMPORTANT: (1) is NOT a tuple — it's just the integer 1!
print(type((1)))    # → <class 'int'>
print(type((1,)))   # → <class 'tuple'>

# Tuple slicing works exactly like list slicing
print(tup[1:4])     # → (64, 33, 95)
print(tup[::-1])    # → (76, 95, 33, 64, 87)


# ============================================================
# 🔧 TUPLE METHODS
# ============================================================

# Tuples have only 2 methods (can't modify, so no add/remove methods)

tup = (2, 1, 3, 1)

# index(el) — returns index of FIRST occurrence of element
print(tup.index(1))   # → 1  (first '1' is at index 1)
print(tup.index(3))   # → 2  (3 is at index 2)

# count(el) — counts TOTAL occurrences of an element
print(tup.count(1))   # → 2  (1 appears twice)
print(tup.count(3))   # → 1  (3 appears once)
print(tup.count(9))   # → 0  (9 doesn't exist, no error)


# ============================================================
# 📖 DICTIONARY IN PYTHON
# ============================================================

# Dictionaries store data as key:value pairs
# They are UNORDERED and MUTABLE
# Keys must be UNIQUE — duplicate keys are overwritten
# Syntax: {key: value, key: value, ...}

student = {
    "name": "Shradha",       # string key → string value
    "cgpa": 9.6,             # string key → float value
    "marks": [98, 97, 95],   # string key → list value (any type works!)
    "age": 20                # string key → integer value
}

print(student)                  # prints entire dictionary
print(student["name"])          # → Shradha
print(student["cgpa"])          # → 9.6
print(student["marks"])         # → [98, 97, 95]
print(student["marks"][0])      # → 98  (indexing into list inside dict)


# ADDING / UPDATING values in a dictionary

student["city"] = "Delhi"    # adds a NEW key-value pair
student["cgpa"] = 9.8        # UPDATES existing key (overwrites old value)
print(student)


# NESTED DICTIONARIES — a dictionary inside another dictionary

student2 = {
    "name": "Arjun",
    "score": {               # value is itself a dictionary!
        "chem": 98,
        "phy": 97,
        "math": 95
    }
}

print(student2["score"])              # → {'chem': 98, 'phy': 97, 'math': 95}
print(student2["score"]["math"])      # → 95  (chain [] to go deeper)
print(student2["score"]["chem"])      # → 98


# ============================================================
# 🔧 DICTIONARY METHODS
# ============================================================

myDict = {"name": "Karan", "age": 21, "city": "Mumbai"}

# keys() — returns all KEYS of the dictionary
print(myDict.keys())    # → dict_keys(['name', 'age', 'city'])

# values() — returns all VALUES of the dictionary
print(myDict.values())  # → dict_values(['Karan', 21, 'Mumbai'])

# items() — returns all (key, value) pairs as tuples
print(myDict.items())   # → dict_items([('name', 'Karan'), ('age', 21), ...])

# get(key) — safely returns value; returns None if key doesn't exist
print(myDict.get("name"))     # → Karan
print(myDict.get("marks"))    # → None  (no error unlike myDict["marks"])
# myDict["marks"]             # ❌ KeyError! Key doesn't exist

# update(newDict) — inserts or updates items from another dictionary
newInfo = {"country": "India", "age": 22}   # "age" will be updated
myDict.update(newInfo)
print(myDict)   # → age is now 22, country added as new key


# ============================================================
# 🔵 SET IN PYTHON
# ============================================================

# A set is an UNORDERED collection of UNIQUE & IMMUTABLE elements
# Duplicate values are automatically removed
# Sets use {} but WITHOUT key:value pairs

nums = {1, 2, 3, 4}          # basic set
print(nums)                    # → {1, 2, 3, 4}

set2 = {1, 2, 2, 2}           # duplicates automatically removed
print(set2)                    # → {1, 2}

# Creating an empty set — must use set(), NOT {}
null_set = set()               # ✅ correct: empty set
empty_dict = {}                # ❌ this creates an empty DICTIONARY, not set!

print(type(null_set))    # → <class 'set'>
print(type(empty_dict))  # → <class 'dict'>

# Sets are UNORDERED — no guaranteed print order
cities = {"Delhi", "Mumbai", "Bangalore", "Delhi"}
print(cities)    # → {'Mumbai', 'Delhi', 'Bangalore'}  (order may vary, no duplicate)


# ============================================================
# 🔧 SET METHODS
# ============================================================

s = {1, 2, 3}

# add(el) — adds a single element to the set
s.add(4)
print(s)    # → {1, 2, 3, 4}

s.add(2)    # adding existing element → no change (duplicates ignored)
print(s)    # → {1, 2, 3, 4}

# remove(el) — removes a specific element (gives KeyError if not found!)
s.remove(3)
print(s)    # → {1, 2, 4}
# s.remove(99)  # ❌ KeyError if 99 doesn't exist

# pop() — removes and returns a RANDOM element (sets are unordered)
s2 = {10, 20, 30}
val = s2.pop()
print(val)   # some random value from the set
print(s2)    # remaining elements

# clear() — removes ALL elements from the set
s3 = {10, 20, 30}
s3.clear()
print(s3)   # → set()  (empty set)


# UNION & INTERSECTION

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# union(set2) — combines ALL values from BOTH sets (no duplicates)
result = set_a.union(set_b)
print(result)    # → {1, 2, 3, 4, 5, 6}

# intersection(set2) — returns only COMMON values (in both sets)
result2 = set_a.intersection(set_b)
print(result2)   # → {3, 4}


# ============================================================
# 💡 EXTRA EXAMPLES
# ============================================================

# Example 1: Check if element exists using 'in'
fruits = ["apple", "banana", "mango"]
print("apple" in fruits)    # → True
print("grape" in fruits)    # → False

my_set = {10, 20, 30}
print(20 in my_set)         # → True

my_dict = {"a": 1, "b": 2}
print("a" in my_dict)       # → True  ('in' checks KEYS in dict)

# Example 2: Convert between types
lst = [1, 2, 2, 3, 3, 3, 4]
unique_lst = list(set(lst))   # set removes duplicates → convert back to list
print(unique_lst)             # → [1, 2, 3, 4]  (order may vary)

# Example 3: max, min, sum work on lists
numbers = [45, 12, 87, 34, 56]
print("Max:", max(numbers))   # → 87
print("Min:", min(numbers))   # → 12
print("Sum:", sum(numbers))   # → 234

# Example 4: Zip two lists into a dictionary
keys = ["name", "age", "city"]
values = ["Riya", 22, "Pune"]
info = dict(zip(keys, values))    # pairs key[i] with values[i]
print(info)                        # → {'name': 'Riya', 'age': 22, 'city': 'Pune'}

# Example 5: Merge two dictionaries (Python 3.9+ shorthand)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}    # ** unpacks both dicts into a new one
print(merged)                   # → {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Example 6: Difference between sort() and sorted()
nums = [3, 1, 4, 1, 5, 9]
nums.sort()                    # modifies original list IN PLACE
print(nums)                    # → [1, 1, 3, 4, 5, 9]

nums2 = [3, 1, 4, 1, 5, 9]
new = sorted(nums2)            # returns a NEW sorted list, original unchanged
print(nums2)                   # → [3, 1, 4, 1, 5, 9]  ← unchanged
print(new)                     # → [1, 1, 3, 4, 5, 9]


# ============================================================
# 🏋️ PRACTICE QUESTIONS (From Lecture)
# ============================================================

# Q1. Ask user to enter names of 3 favorite movies & store in a list
movies = []                              # start with empty list
for i in range(3):
    movie = input(f"Enter movie {i+1}: ")
    movies.append(movie)                 # add each movie to the list
print("Your favorite movies:", movies)


# Q2. Check if a list contains a palindrome of elements
# (same forwards and backwards)
lst = [1, 2, 3, 2, 1]
reversed_lst = lst.copy()    # copy() so we don't modify the original
reversed_lst.reverse()        # reverse the copy
if lst == reversed_lst:
    print("Palindrome! ✅")
else:
    print("Not a palindrome ❌")

# Test with non-palindrome
lst2 = [1, 2, 3, 4]
reversed_lst2 = lst2.copy()
reversed_lst2.reverse()
print(lst2 == reversed_lst2)   # → False


# Q3. Count students with "A" grade, then sort grades from A to D
grades_tuple = ("C", "D", "A", "A", "B", "B", "A")

count_A = grades_tuple.count("A")    # count() works on tuples too!
print(f"Students with A grade: {count_A}")    # → 3

grades_list = list(grades_tuple)     # convert tuple to list so we can sort
grades_list.sort()                   # sorts alphabetically: A < B < C < D
print("Sorted grades:", grades_list) # → ['A', 'A', 'A', 'B', 'B', 'C', 'D']


# Q4. Store word meanings in a Python dictionary
# (one word can have multiple meanings → use a list as value)
word_dict = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": ["a small animal"]
}
print(word_dict["table"])    # → ['a piece of furniture', 'list of facts & figures']
print(word_dict["cat"])      # → ['a small animal']


# Q5. How many classrooms are needed by all students?
# (1 classroom per unique subject)
subjects = ["python", "java", "C++", "python", "javascript",
            "java", "python", "java", "C++", "C"]

unique_subjects = set(subjects)           # set auto-removes duplicates
print("Unique subjects:", unique_subjects)
print("Classrooms needed:", len(unique_subjects))   # → 5


# Q6. Enter marks of 3 subjects and store in a dictionary
marks_dict = {}    # start with empty dictionary
for i in range(3):
    subject = input("Enter subject name: ")
    mark = float(input(f"Enter marks for {subject}: "))
    marks_dict[subject] = mark      # add subject:marks pair to dict
print("Your marks:", marks_dict)


# Q7. Store 9 and 9.0 as SEPARATE values in a set
# Problem: In Python, 9 == 9.0 is True, so sets treat them as the same!
# print({9, 9.0})  → {9}   (only one stored!)
# Solution: Wrap them in tuples to differentiate by type
tricky_set = {("int", 9), ("float", 9.0)}
print(tricky_set)   # → {('int', 9), ('float', 9.0)}  ← both stored!


# ============================================================
# 🌟 BONUS QUESTIONS
# ============================================================

# B1. Remove duplicates from a list while PRESERVING order
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
seen = set()           # track what we've already added
unique_ordered = []
for item in lst:
    if item not in seen:
        unique_ordered.append(item)
        seen.add(item)
print("Original:", lst)
print("Without duplicates:", unique_ordered)   # → [3, 1, 4, 5, 9, 2, 6]


# B2. Find students common to two classrooms (set intersection)
class_A = {"Rahul", "Priya", "Amit", "Sara"}
class_B = {"Priya", "Neha", "Amit", "Rohan"}
common = class_A.intersection(class_B)
print("Students in both classes:", common)   # → {'Priya', 'Amit'}

all_students = class_A.union(class_B)
print("All unique students:", all_students)  # → all 6 names


# B3. Count frequency of each element in a list using a dictionary
lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
freq = {}                    # empty dictionary to store counts
for item in lst:
    if item in freq:
        freq[item] += 1      # increment count if key exists
    else:
        freq[item] = 1       # create new key with count 1
print("Frequency:", freq)    # → {1: 1, 2: 2, 3: 3, 4: 4}


# B4. Check if two lists have any common elements (using sets)
list1 = [1, 2, 3, 4]
list2 = [5, 6, 3, 7]
common_elements = set(list1).intersection(set(list2))
if common_elements:
    print("Common elements found:", common_elements)   # → {3}
else:
    print("No common elements")