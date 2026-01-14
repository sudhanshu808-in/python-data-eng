from loguru import logger

list = [1,2,3,4,5,6,7,8,9,10]

tmp = 0
for a in list :
    print(f"This is in {tmp} : {a}")
    tmp=tmp+1


for i in range(len(list)):
    print(f"value of i  : {i}")


for i in range(5):
    print("* "*(i+1))

print("\n")

for i in range(5):
    print("* "*(5-i))