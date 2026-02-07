# A set is an unordered collection of unique elements.
# Sets are mutable, meaning you can add or remove elements from them.
# Sets are defined by enclosing comma-separated elements in curly braces {}.
# Duplicate elements are automatically removed.

# --- Creating a Set ---
# Creating a set from a list of integers
my_set = {1, 2, 3, 4, 5, 2, 3}  # Duplicates 2 and 3 are ignored
print(f"Initial set: {my_set}") # Output: {1, 2, 3, 4, 5}

# Creating a set from a string
char_set = set("hello world")
print(f"Set from a string: {char_set}") # Output: {'l', 'o', 'd', 'h', ' ', 'w', 'e', 'r'} (order may vary)

# Creating an empty set
# Note: {} creates an empty dictionary, not an empty set.
empty_set = set()
print(f"An empty set: {empty_set}")


# --- Set Operations ---

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# 1. Union (| or .union())
# The union of two sets is a set containing all elements from both sets.
union_set = set_a | set_b
print(f"Union of A and B: {union_set}") # Output: {1, 2, 3, 4, 5, 6, 7, 8}
# Alternative method:
# union_set = set_a.union(set_b)


# 2. Intersection (& or .intersection())
# The intersection of two sets is a set containing only the elements that are common to both.
intersection_set = set_a & set_b
print(f"Intersection of A and B: {intersection_set}") # Output: {4, 5}
# Alternative method:
# intersection_set = set_a.intersection(set_b)


# 3. Difference (- or .difference())
# The difference of set A and set B is a set containing elements that are in A but not in B.
difference_set = set_a - set_b
print(f"Difference of A - B: {difference_set}") # Output: {1, 2, 3}
# The order matters:
difference_set_ba = set_b - set_a
print(f"Difference of B - A: {difference_set_ba}") # Output: {8, 6, 7}
# Alternative method:
# difference_set = set_a.difference(set_b)


# 4. Symmetric Difference (^ or .symmetric_difference())
# The symmetric difference is a set containing elements that are in either set, but not in both.
# It is the opposite of the intersection.
sym_diff_set = set_a ^ set_b
print(f"Symmetric Difference of A and B: {sym_diff_set}") # Output: {1, 2, 3, 6, 7, 8}
# Alternative method:
# sym_diff_set = set_a.symmetric_difference(set_b)


# --- Modifying a Set ---

# 1. .add(element)
# Adds a single element to the set. If the element is already present, it does nothing.
my_set.add(6)
print(f"Set after adding 6: {my_set}") # Output: {1, 2, 3, 4, 5, 6}

# 2. .update(iterable)
# Adds all elements from an iterable (like a list, tuple, or another set) to the set.
my_set.update([7, 8, 9])
print(f"Set after updating with [7, 8, 9]: {my_set}") # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 3. .remove(element)
# Removes a specified element. Raises a KeyError if the element is not found.
my_set.remove(9)
print(f"Set after removing 9: {my_set}")
# The following line would cause an error:
# my_set.remove(99) # KeyError: 99

# 4. .discard(element)
# Removes a specified element. Does NOT raise an error if the element is not found.
my_set.discard(8)
print(f"Set after discarding 8: {my_set}")
my_set.discard(99) # No error is raised
print(f"Set after discarding a non-existent element (99): {my_set}")

# 5. .pop()
# Removes and returns an arbitrary element from the set.
# Since sets are unordered, you don't know which element will be popped.
popped_element = my_set.pop()
print(f"Popped element: {popped_element}")
print(f"Set after pop: {my_set}")

# 6. .clear()
# Removes all elements from the set.
my_set.clear()
print(f"Set after clearing: {my_set}") # Output: set()


# --- Other Useful Set Methods ---

# 1. Membership Testing ('in' keyword)
# Check if an element exists in a set. This is very fast.
fruits = {"apple", "banana", "cherry"}
print(f"Is 'banana' in fruits? {'banana' in fruits}") # Output: True
print(f"Is 'mango' in fruits? {'mango' in fruits}") # Output: False

# 2. len()
# Get the number of elements in a set.
print(f"Number of fruits: {len(fruits)}") # Output: 3

# 3. Subsets and Supersets
# .issubset() - Checks if all elements of a set are present in another set.
# .issuperset() - Checks if a set contains all elements of another set.
set_c = {1, 2}
set_d = {1, 2, 3, 4}
print(f"Is C a subset of D? {set_c.issubset(set_d)}") # Output: True
print(f"Is D a superset of C? {set_d.issuperset(set_c)}") # Output: True


# --- Use Cases for Sets ---
# 1. Removing duplicates from a list.
my_list = [1, 2, 2, 3, 4, 4, 4, 5]
unique_elements = list(set(my_list))
print(f"List with duplicates removed: {unique_elements}")

# 2. Fast membership testing.
# Checking for an element in a set is much faster on average than in a list.
large_list = list(range(1_000_000))
large_set = set(range(1_000_000))

# The following check is much faster with the set.
# 'in' on a list: O(n) - has to check each element on average.
# 'in' on a set: O(1) - uses a hash table for near-instant lookup.
print(f"999,999 in large_set: {999999 in large_set}")
