def factors(n):
    flist=[]
    for i in range(1,n+1):
        if n%i==0:
            flist=flist+[i]
        if flist==[1,n]:
                print("it is true ")
            else:
                print("It is not prime ")
    return flist




factors(99)


