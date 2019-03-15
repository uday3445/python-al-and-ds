l1=[2,4,6,8]

l2=[2,4,6,8]

l3=l2


"""
l1 and l2 are two lists with same value 
l2 and l3 are same list with different names

x==y cheks if x and y have same values
x is y cheks if x and y refer to same object
"""

print("the l1 and l2 have same value ",l1==l2)
print("the l2 and l3 have same value ",l2==l3)
print("the l1 and l2 refer to same object ",l1 is l2)
print("the l2 and l3 refers to same object ",l2 is l3)