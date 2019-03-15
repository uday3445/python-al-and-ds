''''
lists can also be concatinated by using +
'''

l1=[1,3,5,7]
l2=[2,4,6,8]
l3 =l1+l2
print(l3)


m1=[1,3,5,7]
m2=m1
print("The list m2 is ", m2)
m1=m1+[9]
print("The modified list m1 is ",m1)
print("The modified list m2 is ",m2)