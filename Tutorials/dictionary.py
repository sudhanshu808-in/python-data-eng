# This script demonstrates various operations on Python dictionaries.

print("\n")
# Creating a dictionary in Python
# A dictionary is a collection of key-value pairs.
dict = {
    "name" : "sudhanshu",
     "age" :22
}

# inserting new key-value pairs into the dictionary
# We can add new elements to a dictionary by assigning a value to a new key.
dict["subjects"]=["ML","DL","AI"]

print(dict)

#accessing the elements 
# We can access the value of a specific key using square brackets.
print("\n")
print(dict["subjects"])
print(dict["name"])
print(dict["age"])

# New dict
# Here is another example of a dictionary.
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

#accessing keys , output is list of keys 
# The .keys() method returns a view object that displays a list of all the keys in the dictionary.
print(salaries.keys())

#accessing values in form of list the output comes
# The .values() method returns a view object that displays a list of all the values in the dictionary.
print(salaries.values())

#accessing items here they are in form of tuples 
# The .items() method returns a view object that displays a list of a dictionary's key-value tuple pairs.
print(salaries.items())


# iterating through the tuples , not mendatory to say key it can be any variable name 
# We can iterate through the keys of a dictionary using a for loop.
for key in salaries:
    print(f"{key} : {salaries[key]}")

# another method is that to use the tuples form like () which is returned by .items()
# We can also iterate through the key-value pairs of a dictionary using the .items() method.
for key,value in salaries.items():
    print(f"{key} -- : -- {value}")

# new dictinoary
# This is an example of a nested dictionary.
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

# Iterating through the nested dictionary to get the role of each data engineer.
for key in data_engineers:
    print(f"{key} : {data_engineers[key]["role"]}")
    
# Iterating through the nested dictionary to get the tools used by each data engineer.
for key,value in data_engineers.items():
    print(f"{key} : --->  {value["tools"]}")
    
#nested ones
# Another example of a nested dictionary.
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

# Iterating through the nested dictionary to get the role of each data engineer.
for i in range(len(data_engineers2["data"])):
    print(f"{data_engineers2["data"][i]["role"]}")