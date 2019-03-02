def gcd(m,n):
    cf=[]
    for i in range (1,min(m,n)+1):
        if (m%i)==0 and (n%i)==0:
            cf.append(i)
    return( cf[-1])
num1 = int(input("The first number  is "))
num2 = int(input("The second number is  "))
print('the gcd of  ', num1, 'and ', num2, 'is ',  gcd(num1, num2))

