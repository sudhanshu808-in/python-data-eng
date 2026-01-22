print("\n")
# Creating a dictionary in Python
dict = {
    "name" : "sudhanshu",
     "age" :22
}

# inserting new key-value pairs into the dictionary
dict["subjects"]=["ML","DL","AI"]

print(dict)

#accessing the elements 
print("\n")
print(dict["subjects"])
print(dict["name"])
print(dict["age"])

# New dict
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
print(salaries.keys())

#accessing values in form of list the output comes
print(salaries.values())

#accessing items here they are in form of tuples 
print(salaries.items())


# iterating through the tuples , not mendatory to say key it can be any variable name 
for key in salaries:
    print(f"{key} : {salaries[key]}")

# another method is that to use the tuples form like () which is returned by .items()
for key,value in salaries.items():
    print(f"{key} -- : -- {value}")

# new dictinoary

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


for key in data_engineers:
    print(f"{key} : {data_engineers[key]["role"]}")
    

for key,value in data_engineers.items():
    print(f"{key} : --->  {value["tools"]}")
    
#nested ones

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


for i in range(len(data_engineers2["data"])):
    print(f"{data_engineers2["data"][i]["role"]}")