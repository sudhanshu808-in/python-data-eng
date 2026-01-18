# # from loguru import logger

# # list = [1,2,3,4,5,6,7,8,9,10]

# # tmp = 0
# # for a in list :
# #     print(f"This is in {tmp} : {a}")
# #     tmp=tmp+1


# # for i in range(len(list)):
# #     print(f"value of i  : {i}")


# # for i in range(5):
# #     print("* "*(i+1))

# # print("\n")

# # for i in range(5):
# #     print("* "*(5-i))


# # arr =[1,2,3,4,5,6,7,8,9,10]
# # for i in range(len(arr)):
# #     print(f"this is the value of {i} : {arr[i]}")


# # str= "Python is a powerful programming language that is easy to learn and fun to use. Many developers love Python because Python allows them to write clean and readable code. In data science, Python is used for data analysis, data visualization, and machine learning. Web developers also use Python to build backend services and APIs. Even beginners choose Python because the Python syntax is simple and Python programs are easy to understand."

# # words = str.split()

# # # print(len(words))

# # c=0

# # for i in range(len(words)):
# #     if(words[i]=="Python"):
# #         c=c+1

# # print(f"the number of ------ : {c}")

# arr=[202,165,89,76,12]
# number = -121
# print(len(arr))
# index=-1
# for i in range(len(arr)):
#     if(number>arr[0]):
#         index=0
#         break
#     if(i==len(arr)-1 and arr[i]>number):
#         index=i+1
#         break
#     # print(f" i : {i}  : : {arr}")
#     if(arr[i]>=number and number>=arr[i+1]):
#         index=i+1
#         break

# arr.insert(index,number)
# print(arr)
# print(len(arr))


#list comprehension
sample = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#when only if is there true condition will be before  "for" and  "if" after for
newSample = ["Yeah" for i in range(len(sample)) if sample[i]%2==0 ]

#when both if and else is needed then they will be before the "for" Loop
extraSample = ["Yeah"if i%2==0 else "LOL dAyum" for i in range(len(sample)) ]

print(len(extraSample))
print(len(newSample))