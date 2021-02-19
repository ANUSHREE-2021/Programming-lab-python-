def factorial(n):
    if n==0:
        return 1
    else:
        fact = factorial(n-1)
        fact1 = n * fact
        return fact1
sum=0
limit = int(input("enter the limit: "))
for n in range(1, limit):
    if n%2!=0:
        result = n/(factorial(n))
        sum = sum + result
print("sum=",sum)