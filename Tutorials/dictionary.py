# A dictionary is a collection of key-value pairs. 
# It is an unordered, mutable, and indexed collection.
# In Python, dictionaries are written with curly brackets {}.
print("\n")

# Creating a dictionary in Python.
# The keys are "name" and "age", and the values are "sudhanshu" and 22.
dict = {
    "name" : "sudhanshu",
     "age" :22
}

# Inserting new key-value pairs into the dictionary.
# The key is "subjects" and the value is a list of strings.
dict["subjects"]=["ML","DL","AI"]

# Printing the entire dictionary.
print(dict)

# Accessing the elements of a dictionary.
# You can access the value of a key by using the key in square brackets [].
print("\n")
print(dict["subjects"])
print(dict["name"])
print(dict["age"])

# A new dictionary called 'salaries' is created.
# The keys are names of people and the values are their salaries.
salaries = {
    "shubham": 25000,
    "rahul": 32000,
    "ankit": 28000,
    "priya": 35000,
    "neha": 30000,
    "aman": 27000,
    "rohit": 40000,
    "sneha": 33000,
    "vikas": 29000,
    "kavya": 36000,
    "arjun": 45000
}

# The .keys() method returns a view object that displays a list of all the keys in the dictionary.
print(salaries.keys())

# The .values() method returns a view object that displays a list of all the values in the dictionary.
print(salaries.values())

# The .items() method returns a view object that displays a list of a dictionary's key-value tuple pairs.
print(salaries.items())


# Iterating through the keys of the dictionary.
# For each key in the 'salaries' dictionary, it prints the key and its corresponding value.
# It is not mandatory to use 'key' as the variable name; any valid variable name will work.
for key in salaries:
    print(f"{key} : {salaries[key]}")

# Another method to iterate through a dictionary is to use the .items() method.
# This method returns key-value pairs as tuples.
# We can unpack the tuples into two variables, 'key' and 'value'.
for key,value in salaries.items():
    print(f"{key} -- : -- {value}")

# A new dictionary called 'data_engineers' is created.
# This is a nested dictionary where the values are themselves dictionaries.
data_engineers = {
    "shubham": {
        "role": "Junior Data Engineer",
        "salary": 25000,
        "skills": ["Python", "SQL", "Git"],
        "tools": ["PostgreSQL", "VS Code"],
        "experience_years": 0.5
    },
    "aman": {
        "role": "Data Engineer",
        "salary": 45000,
        "skills": ["Python", "SQL", "Spark", "Airflow"],
        "tools": ["AWS", "S3", "Redshift"],
        "experience_years": 2
    },
    "priya": {
        "role": "Senior Data Engineer",
        "salary": 85000,
        "skills": ["Python", "Scala", "Kafka", "Spark"],
        "tools": ["GCP", "BigQuery", "Dataflow"],
        "experience_years": 5
    },
    "hrithik": {
        "role": "ETL Engineer",
        "salary": 60000,
        "skills": ["Python", "SQL", "Airflow"],
        "tools": ["MySQL", "Snowflake"],
        "experience_years": 3
    }
}


# Iterating through the 'data_engineers' dictionary.
# For each key, it prints the key and the value of the 'role' key from the nested dictionary.
for key in data_engineers:
    print(f"{key} : {data_engineers[key]["role"]}")
    

# Iterating through the 'data_engineers' dictionary using .items().
# For each key-value pair, it prints the key and the value of the 'tools' key from the nested dictionary.
for key,value in data_engineers.items():
    print(f"{key} : --->  {value["tools"]}")
    
# This is another example of a nested dictionary.
# The top-level key is "data", and its value is another dictionary.
# The keys of the inner dictionary are integers (0, 1, 2, 3), and the values are dictionaries containing information about data engineers.
data_engineers2= {
   "data" : { 0: {
        "role": "Junior Data Engineer",
        "salary": 25000,
        "skills": ["Python", "SQL", "Git"],
        "tools": ["PostgreSQL", "VS Code"],
        "experience_years": 0.5
    },
    1: {
        "role": "Data Engineer",
        "salary": 45000,
        "skills": ["Python", "SQL", "Spark", "Airflow"],
        "tools": ["AWS", "S3", "Redshift"],
        "experience_years": 2
    },
    2: {
        "role": "Senior Data Engineer",
        "salary": 85000,
        "skills": ["Python", "Scala", "Kafka", "Spark"],
        "tools": ["GCP", "BigQuery", "Dataflow"],
        "experience_years": 5
    },
    3: {
        "role": "ETL Engineer",
        "salary": 60000,
        "skills": ["Python", "SQL", "Airflow"],
        "tools": ["MySQL", "Snowflake"],
        "experience_years": 3
    }}
}


# Iterating through the nested dictionary 'data_engineers2'.
# It uses a for loop with a range function to iterate from 0 to the length of the inner dictionary.
# For each iteration, it prints the value of the 'role' key from the nested dictionary.
for i in range(len(data_engineers2["data"])):
    print(f"{data_engineers2["data"][i]["role"]}")