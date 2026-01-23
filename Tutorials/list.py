# This script demonstrates various operations on Python lists.

# Example of creating lists for names and salaries.
names = ["shubham" ,"sk","pk","dk"]
salary = [1000,1200,1500,3000]

# Example of concatenating two lists.
# The '+' operator creates a new list containing all elements from both lists.
print("Concatenated list:", names + salary)

# Accessing elements by their index. In Python, list indices start at 0.
print("First name:", names[0]) # Accesses the first element: "shubham"
print("Second name:", names[1]) # Accesses the second element: "sk"

# The insert() method adds an element at a specified position.
names.insert(1,"himanshu") # Inserts "himanshu" at index 1
salary.insert(1,1900)   # Inserts 1900 at index 1

# Displaying the lists after insertion.
print("Lists after insertion:", names, salary)

# Slicing a list to reverse parts of it.
# The format is [start:stop:step]. A step of -1 reverses the order.
# This slice starts at index 4, goes to index 0 (exclusive), and steps backward.
print("Reversed part of salary list:", salary[4:0:-1])

# A common Python trick to reverse an entire list using slicing.
print("Reversed names list:", names[::-1])
 # Example of a new list with integers.
new_list = [1,2,3,4,5,4,6,7,8,9]

# The len() function returns the number of elements in a list.
print("Length of new_list:", len(new_list))

# The remove() method removes the first occurrence of a specified value.
new_list.remove(4) # Removes the first '4' it finds
print("new_list after removing 4:", new_list)

# Checking the length of the list after removing an element.
print("Length of new_list after removing an element:", len(new_list))

# The pop() method removes the element at a specified index and returns it.
# If no index is specified, it removes and returns the last item.
popped_value = new_list.pop(4)
print(f"This is the poped value : ->{popped_value}")

# Displaying the list after the pop operation.
print("new_list after pop:", new_list)

# Lists are mutable, meaning their elements can be changed.
new_list[0]="shubham" # Replaces the element at index 0 with "shubham"
print("new_list after changing an element:", new_list)

# The 'del' keyword removes an element at a specified index.
del new_list[0]
print("new_list after deleting an element:", new_list)

# A string representing a RESTful API endpoint URL.
api_endpoint= "https://api.datastreamx.io/v1/platforms/enterprise/clients/482193/projects/alpha-ml/pipelines/ingestion/runs/2025/01/07/execution/9f3a7c2e4b1d8a6f5e0c9d2a4b7e6f1a/nodes/source/s3/bucket/raw-data/events/partition/year=2025/month=01/day=07/region=ap-south-1/format=json/schema/v3/metrics/throughput/latency/erros"

# The split() method breaks a string into a list of substrings.
# Here, it's used to segment the URL by the '/' character.
new_list = api_endpoint.split("/")

# Prints the list of URL segments.
print("URL segments:", new_list)
