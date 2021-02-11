def perfect_num(n):
    
    sum = 0


    for x in range(1,n):
        if n%x == 0:
            sum = sum + x
    return sum == n


num = int(input("enter the number: "))

if (perfect_num(num)):
    print("perfect number")
else:
    print("not perfect")
