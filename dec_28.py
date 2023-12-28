# # methods vs. functions
# # function_name(oprand)
# # oprand.method_name(arguments)
#
# # Case related methods:
# #slice
# s1='ROYAL TECHNOSOFT limited'


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
# s2=s1[:5]
# s3=s1[-7:]
# print(f"{s2} {s3}")
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
s1='students .of this batch are going to rock the INDIAN software industry!'
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
s1='students .of this batch are going to rock the INDIAN software industry!'
print(s1)
print(s1.capitalize())
# # print(len(s1))
# # # print(s2)	# strings are immutable so, methods of strings cannot change the original string. Instead, they will return a new string.
# # print( s1.capitalize())
# # # # print( s1[5].capitalize())
print(s1.upper())
print(s1.lower())
print(s1.swapcase())
print(s1.title())


# len(s1)
# print()
# input()
# type()

s1 = 'stDudents of this batch are going to rock the INDIAN software industry?'
# s2 = "What is ß"

# print(s2.lower())
# print(s1)
# print(s1.casefold())

s1 = 'stDudents of this batch are going to rock the INDIAN software industry?'

# s3 = s1.center()
# print(s1.center(100,"*"))
# print(s1.rjust(100, "*"))
# print(s1.ljust(100, "-"))
#
# print("|" + "Welcome to our software!".center(100) + "|")
# print(s3)

# Alignment related methods
"""
s3 = s1.center(100)
print(s1.center(100, "-"))
print(s1.rjust(100, "*"))
print(s1.ljust(100, "-"))

print("-" * 102)
print("|" + "Welcome to our software!".center(100) + "|")
print("-" * 102)
"""
s1 = 'e estDudents of this batch are egoing to rock the INDIAN software industry?'
print(s1.count("e e",10,50))

# print(s1.count("are"))
# print(s1.count("europe"))
#
# print(s1.count("z", 20))
# print(s1.count("e", 20, 40))
