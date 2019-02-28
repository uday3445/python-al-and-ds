def gcd(m, n):
    fm = []
    for i in range(1,m+1):
        if (m % i) == 0:
            fm.append(i)

    fn = []
    for i in range(1, n+1):
        if (n % i) == 0:
            fn.append(i)
    cf = []
    for i in fm:
        if i in fn:
            cf.append(i)
    return(cf)


num1 = int(input("The first number  is "))
num2 = int(input("The second number is  "))
print('the gcd of  ', num1, 'and ', num2, 'is ',  gcd(num1, num2))



