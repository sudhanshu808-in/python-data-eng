from loguru import logger

# It's a best practice to not use variable names that shadow built-in types like 'list'.
my_list = [1,2,3,4,5,6,7,8,9,10]

# --- Basic For Loop ---
# This loop iterates through each element in 'my_list'.
# A separate counter 'tmp' is used to track the index.
logger.info("--- Basic For Loop ---")
tmp = 0
for a in my_list :
    print(f"This is in {tmp} : {a}")
    tmp=tmp+1
# A more "Pythonic" way to do this is using the enumerate() function:
logger.info("--- Using enumerate() ---")
for index, value in enumerate(my_list):
    print(f"This is in {index} : {value}")


# --- Loop using range() and len() ---
# This loop iterates through the indices of the list, from 0 to len(my_list)-1.
logger.info("--- Loop using range() and len() ---")
for i in range(len(my_list)):
    # This only prints the index, not the value at that index.
    print(f"value of i  : {i}")


# --- Nested Loops for Pattern Printing ---
# This loop prints an increasing number of asterisks for each row.
logger.info("--- Pattern Printing ---")
for i in range(5):
    # (i+1) ensures the pattern starts with one asterisk.
    print("* "*(i+1))

print("\n") # Adds a newline for separation.

# This loop prints a decreasing number of asterisks for each row.
for i in range(5):
    # (5-i) creates the inverted pyramid effect.
    print("* "*(5-i))


# --- Accessing elements by index in a loop ---
arr =[1,2,3,4,5,6,7,8,9,10]
logger.info("--- Accessing elements by index in a loop ---")
for i in range(len(arr)):
    # This correctly prints both the index 'i' and the value 'arr[i]'.
    print(f"this is the value of {i} : {arr[i]}")


# --- String Manipulation and Loop ---
# Avoid using 'str' as a variable name as it shadows the built-in string type.
logger.info("--- String Manipulation and Loop ---")
my_str= "Python is a powerful programming language that is easy to learn and fun to use. Many developers love Python because Python allows them to write clean and readable code. In data science, Python is used for data analysis, data visualization, and machine learning. Web developers also use Python to build backend services and APIs. Even beginners choose Python because the Python syntax is simple and Python programs are easy to understand."

# Splits the string into a list of words based on whitespace.
words = my_str.split()

print(f"Total number of words: {len(words)}")

# This loop counts the occurrences of the word "Python".
count = 0
for i in range(len(words)):
    if(words[i]=="Python"):
        count=count+1

print(f"The word 'Python' appears {count} times.")


# --- Inserting an element into a sorted list (descending) ---
logger.info("--- Inserting an element into a sorted list (descending) ---")
arr=[202,165,89,76,12]
number = -121
print(f"Original array length: {len(arr)}")
index=-1 # Initialize index to -1 (or a sentinel value)

for i in range(len(arr)):
    # Case 1: The number is larger than the biggest element in the list.
    if(number>arr[0]):
        index=0
        break
    # Case 2: We've reached the end, and the number is the smallest.
    if(i==len(arr)-1 and arr[i]>number):
        index=i+1
        break
    # Case 3: Found the correct position between two elements.
    # We need to check i+1, so we must be careful not to go out of bounds.
    # This check is safe because the previous 'if' handles the last element.
    if(arr[i]>=number and number>=arr[i+1]):
        index=i+1
        break

# Insert the number at the determined index.
arr.insert(index,number)
print(f"Array after insertion: {arr}")
print(f"New array length: {len(arr)}")


# --- List Comprehensions ---
# A concise way to create lists.
logger.info("--- List Comprehensions ---")
sample = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# List comprehension with a condition (if).
# Creates a new list containing "Yeah" for each even number in 'sample'.
# [expression for item in iterable if condition]
newSample = ["Yeah" for i in range(len(sample)) if sample[i]%2==0 ]
print("newSample:", newSample)

# List comprehension with a condition (if-else).
# Creates a new list where the value is "Yeah" for even numbers and "LOL dAyum" for odd numbers.
# [expression_if_true if condition else expression_if_false for item in iterable]
extraSample = ["Yeah"if i%2==0 else "LOL dAyum" for i in range(len(sample)) ]
print("extraSample:", extraSample)

print(f"Length of newSample (even numbers): {len(newSample)}")
print(f"Length of extraSample (all numbers): {len(extraSample)}")
