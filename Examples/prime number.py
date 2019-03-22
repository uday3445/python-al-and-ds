"""
prime number :only factor 1 and itself
prime number is the one which is divisible by 1 and it self
"""
def factors(n):
    """

    :param n:
    :return:
    """
    flist=[]
    for i in range (1,n+1):
        if n%i==0:
            flist=flist+[i]
    return (flist)

def isprime(n):
    return (factors(n)==[1,n])

def uprime(n):
    pl=[]
    for i in range(1,n+1):
        if isprime(i):
            pl =pl+[i]
    return (pl)

def nprime(n):
    (count,i,plist)=(0,1,[])
    while(count<n):
        if isprime(i):
            (count,plist)=(count+1,plist+[i])
        i=i+1
    return plist
z =input(print("enter the number"))

c=factors(int(z))

print("the factors of ,",z,"",c)
f=isprime(int(z))
print("is",z,"prime",f)

u=uprime(int(z))
print("list of primes upto",z,"are",u)
print(len(u))

k=nprime(int(z))
print("first ",z," Prime numbers are",k)

