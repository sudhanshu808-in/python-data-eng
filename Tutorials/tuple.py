from loguru import logger

test__tuple = (1,2,3,4,5,6,7,"Shubham")

logger.info(test__tuple)

#cannot add values to tuple

# test__tuple[1] = 56

#if there is only 1 value in the tuple then its type will not be tuple but instead that variabke

print(type((1,2,3,)))
print("\n")
print(type((1)))


#iterating intuple 
print(test__tuple[4:8])

test__tuple = (1,2,1,1,1,1,1,1,1,1,1,1,2,3,4,5,6,7,"Shubham")


print(test__tuple.count(1))

print(test__tuple.index(2))


#Q1 convert  tuple having lists into single tuple

test__tuple = ([5,6], [6,7,8,9], [3])
new_lsit=[]


# #0(n)2
# for  i in test__tuple :
#     for j in i :
#         new_lsit.append(j)

#O(n)
for i in test__tuple :
    new_lsit = new_lsit + i

test__tuple = tuple(new_lsit)
print(test__tuple)




#adding 2 tuples 
tup1 =(1,2,3,3)
tup2 =("shubham", "boi")
tup3 = tup1+tup2
print(tup3)