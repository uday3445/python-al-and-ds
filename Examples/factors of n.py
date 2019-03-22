def prime(n):
    for i in range(2,n+1):
            k=0
            for a in range(2,i//2+1):
                if i%a==0:
                    k=k+1
            if (k<=0):
                print(i)
    return a



j=(prime(10))
prime(j)





