# Write a Python program to calculate a dog's age in dog years.
# Note: For the first two years, a dog year
# is equal to 10.5 human years. After that, each dog year equals 4 human years.
# Expected Output:
# Input a dog's age in human years: 15
# The dog's age in dog's years is 73





# Write a Python program to convert a month name to a number of days.
# Expected Output:

# List of months: January, February, March, April, May, June, July, August
# , September, October, November, December
# Input the name of Month: February
# No. of days: 28/29 days

# inp_str='jan'
# mon_31=['jan','mar','may','jul','sep','oct','dec']

# if inp_str == 'feb':
#     print(28)
# elif inp_str in mon_31:
#     print(31)
# else:
#     print(30)



# looping:
# on string and list


# for i in 'abcd':
#     print(i)

# list1=[1,2,3,4,5,6,7,8,9,10]
# str1 = '12345678910'

# # if complexity is 1
# # for complexcity is n

# for i in str1:
#     print(i)

# for i in list1:
#     print(i)


# str1='12345123456'
# # remove duplicates from this string

# str2="123456"
# list1=[]
# for i in str1:
#     if i not in list1:
#         # str2 =str2+i
#         list1.append(i)
# str3=''.join(list1)
# print(type(str3))
# print(list1)

list1=[11,22,33,44,55,66,77,88,99,00]
# sum of even and odd number from the list1
even =0
odd =0
for i in list1:
    if i % 2== 0:
        even +=i
    else:
        odd+=i

# range()

# list=[1,2,3,..10]

# take input from user and count sum of all odd number from the given range
# list1=[1,2,3,4,5]
# for i in range(len(list1)):
#     # print(list1[i],i)
#     if list1[i] % 2 == 0:
#         print(list1[i])




# break:

# for i in range(100):
#     if i ==10:
#         break
#     print(i)

# for i in range(10):
   
#     if i ==1:
#         continue
#     print(i)


# for i in "happy":
#     pass


# remove duplicates
# abc='1234556' 
# list1=list(abc)
# list2='12345'
# for i in abc:
#     if i not in list2:
#         print(i)
#         list2=list2+i
#
# print(''.join(list2))
# print(list2)
# print(str(list2))

# 