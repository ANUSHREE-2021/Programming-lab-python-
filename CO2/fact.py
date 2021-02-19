num = int(input("Enter the number: "))
fact = 1
if num < 0:
    print("number is negative,factorial cannot be found")
else:
    for n in range(1, num+1):
        fact = fact * n
    print("Factorial =",fact )