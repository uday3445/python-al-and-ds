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


