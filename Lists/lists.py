"""
lists are sequence of values
lista can be of mixed values
"""
m=[5,'uday',0]
print(m[0],"is 5")
print(m[1],'is uday')
print(m[2], "is 0")

mx=[[2,[37]],4,["uday"]]
print(mx[0],"is [2,[37]]")
print(mx[1],"is 4")
print(mx[2],"is  uday")
print(mx[0][1:2],"is [[37]]")

mx[1]=80
print(mx,"is upadted list with 80")

mx[0][1][0]=99
print(mx,"is upadted list with 99")

l1=[8,8,8,8,]
l2=l1

print("ïnitial l2 is ",l2)
l1[2]=9
print("updated list l1 is ",l1)
print("updated list l2 is ",l2)


m1=[4,7,80]
m2=m1[:]
print("The initial M2 is",m2)

m1[2] = 889
print("the modified m1 with 889",m1)
print("The not modidfied m2 with 889" ,m2)