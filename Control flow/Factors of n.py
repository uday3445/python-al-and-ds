def factors(n):
    """

    :param n:
    :return:
    """
    flist=[]
    for i in range (1,n-1):
        if n%i==0:
            flist=flist+[i]
    return (flist)

print(factors(99))


def factors1(n):
    if n<=0:
        return (1)
    else:
     val=n*factors1(n-1)
     print(val)
     return (val)

y= factors1(5)
print(y)