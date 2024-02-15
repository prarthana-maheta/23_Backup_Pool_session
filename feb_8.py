# keywords for looping:
# break
# continue
# pass
# a=10
# list1=[1,2,3,10,3,4,10]
# #
# for i in list1:
#
#     if i==10:
#         pass
#         print(i)
# a=10
# list1=[1,2,10,10,3,4,10]
# for i in range(len(list1[3:5])):
#     print(list1[i])
    # if list1[i] ==10:
        # print(i)

# Write a Python program to count the number of even and odd numbers in a series of numbers
# Sample numbers : numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4



# Write a Python program that prints all the numbers except  3 and 6.
# Note : Use 'continue' statement.
# 36
# 3,6,13,16,23,26,30,31..39, 
# Expected Output : 0 1 2 4 5

# input_range=int(input())
# list1=[]
# for i in range(input_range+1):
#     if '3' in str(i) or '6' in str(i):
#         continue
#     else:
#         list1.append(i)
# print(list1)

# Write a Python program to sum two integers.
# However, if the sum is between 15 and 20 it will return 20.
# a=int(input())
# b=int(input())
# sum=a+b
# for i in range(15,21):
#     if i <= sum:
#         print(20)
#     else:
#         print(sum)

# Write a Python program that checks whether 
        # a string represents an integer or not. 
# Expected Output:
# Input a string: Python1
# The string is  an integer.

# inp_str =input()
# for i in inp_str:
#     if i.isdigit():
#         print("integer")
#         break
#     else:
#         continue 

# # while:
# i=1
# while True:
#     print(i)
#     i +=1
#     if i == 5:
#         break
        # print("---")


# i=0
# while i ==0:
#     print(i)
#     i+=1
# # if i ==1:
# #     for i in range(1,10):
# #         print(i) 
    
# # calculate the sum of five numbers entered by user using while loop
i=0
sum=0

while i<5:
    n = int(input())
    sum+=n
    i+=1
print(sum)