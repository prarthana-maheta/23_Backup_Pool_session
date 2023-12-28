# # a = '1'
# # print(type(a))
# # b=float(a)
# # print(type(b))
# # a=1
# # b=2
# # a,b=b,a
#
#
# # data types:
# #
# # 1 integers -->78952578525852585258515878795455654521
# # 2 float -->1.23456789524522545652452
# # 3 complex --> (1j+1)
# # 4 string --> "hello world",'hello world'
# # 5 list
# # 6 tuple
# # 7 dictionary
# # 8 set
#
#
# # 1) string
# # [1]
# a = 'hello'
# # arr1=[1,2,3,'4',5,6,7,8,9]
# # arr1[3]=10
# # a="hillo"
# # print(arr1)
#
# # # Datatypes in Python:
# # """
# # Numeric: int, float, complex
# # a = 7 + 3i, b = 5 + 7i
# # (7 + 3i)(5 + 7i)
# #
# #
# # a = 7 + 3j
# # b = 5 + 7j
# # print(a * b)
# #
# #
# # collections:
# # string: Ordered & Immutable Collection Of Characters
# # """
s1='Students of this batch are going to rock the INDIAN software industry!'

# index: 	 0123456789..................
# -ve index
# :	 ......................................................987654321
# print(s1[0])
# print(s1[24])
# print(s1[-1])
# print(s1[-3])

# print(s1[100])
# # # print(type(s1))
# # print(s1)
# s2=249
# s2[0]=1
# print(s2)
# s1[0]='1'
# print(s1)
# print(s1[len(s1)-1])


# addition of first and last element
# addition of 5 and last 5 element
# addition of last and second last using len()

# print(f"first and last element are: {s1[0]+s1[-1]}")

s1='Students of this batch are going to rock the INDIAN software industry!'
print(s1[2:-25:-1])
print(s1[-25])
# s2=s1[::]
# print(s1)
# print(s2)


# print alternate chars
# silcing from 10 element to 25 element
# reverse of s1


# from 40 index to -40 using direction -2
#
# from 7 to 37 using negative direction



# s1[len(s1)]
# s2=s1[::69]
# # print(s2)
# # s2=s1[:7:2]
# # print(s1[:7:2])
# # print(s1)
# # print(s2)
# s1="1=====100 fesfsrsdfcfghdre"
#
# # print(s1[:100])
# # s1[0]='1'
# # print(s1)
# # # # slicing
# # s2 = s1[9 : 69]
# # print(s1)	# Slicing will always return new data
# # print(s2)
#
# # print(s1[600])
# # print(s1[12 : 600])
# # print(s1[12 : ])
# # print(s1[ : 60])
# # print(s1[ : ])
#
# # print(s1[60])
# # print(s1[-3])
# """
# print(s1[0])
#
# print(s1[30 : 3])
# print("The end")
# print(s1[-25 : -5])
# print(s1[-30 : 50])
# print(s1[30 : -3])
#
# print(s1[4 : -3])
#
#
# print(s1[3 : 55 : 3])
# print(s1[55 : 3 : -1])
# print(s1[ : : -1])
# print(s1[ : : -3])
# print(String[1:5:2])
# """
#
# # methods vs. functions
# # function_name(oprand)
# # oprand.method_name(arguments)
#
# # Case related methods:
# #slice
# s1='ROYAL TECHNOSOFT limited'
# # s1[]
# # ROYAL
# # TECHNOSOFT
# # limited
# # ROYAL limited
#
#
#
#
#
#
#
# # s2=s1[:5]
# # s3=s1[-7:]
# # print(f"{s2} {s3}")
# # Output:
#
#
#
#
# # *****New task to perform********
#
# s1='strings are IMMUTABLE so, methods of strings cannot change the original string. Instead'
# #
# # Output:- 1) print IMMUTABLE using slicing s1[12:22
# #          2) print Insted using slicing
# #          3) skip alternate character and print the new string
#
# # print(s1[12:22])
# # print(s1[-7:])
# # print(s1[::2])
#
#
# # 'Royal Technosoft Limited'
# # 'I am learning python'
#
# # print(s2)
#
# # indian
# # royal
# # technosoft
# 'Students of this batch are going to rock the INDIAN software industry!'
# s1='students .of this batch are going to rock the INDIAN software industry!'
#
#
# output: s1 bdha first letters capitilize
#         indian in lower case
#         all the s1 string should in upper case
#         all the s1 string should be in lower case
#         software industry  in uppercase
#
# # indian
#
# # s1[5]='abc'
# print(s1)
# print(s1.capitalize())
# # print(len(s1))
# # # print(s2)	# strings are immutable so, methods of strings cannot change the original string. Instead, they will return a new string.
# # print( s1.capitalize())
# # # # print( s1[5].capitalize())
# print(s1.upper())
# print(s1.lower())
# print(s1.swapcase())
# print(s1.title())
#
# len(s1)
# print()
# input()
# type()