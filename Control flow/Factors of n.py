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


print("The cactors are", factors(99))


def factors1(n):
    if n<=0:
        return (1)
    else:
     val=n*factors1(n-1)
     print(val)
     return (val)

def isprime(n):
    return (factors(n)==[1,n])

z=isprime(2)
print(z)



y= factors1(5)
print(y)