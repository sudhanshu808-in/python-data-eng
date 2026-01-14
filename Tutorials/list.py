# names = ["shubham" ,"sk","pk","dk"]
# salary =[1000,1200,1500,3000]

# print(names+salary)

# print(names[1])

# print(names[0])

# names.insert(1,"himanshu")
# salary.insert(1,1900)

# print(names+salary)
# # -1 is like the step u give that is why we need to do the 4:0 as it will go then
# print(salary[4:0:-1])
# #reverse whole
# print(names[::-1])


# new_list = [1,2,3,4,5,4,6,7,8,9]

# print(len(new_list))

# new_list.remove(4)

# print(len(new_list))

# print(f"This is the poped value : ->{new_list.pop(4)}")

# print(new_list)

# new_list[0]="shubham"

# del new_list[0]
# print(new_list)

api_endpoint= "https://api.datastreamx.io/v1/platforms/enterprise/clients/482193/projects/alpha-ml/pipelines/ingestion/runs/2025/01/07/execution/9f3a7c2e4b1d8a6f5e0c9d2a4b7e6f1a/nodes/source/s3/bucket/raw-data/events/partition/year=2025/month=01/day=07/region=ap-south-1/format=json/schema/v3/metrics/throughput/latency/erros"

new_list = api_endpoint.split("/")
print(new_list)