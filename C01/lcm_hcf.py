num1 = int(input('enter the first number: '))
num2 = int(input('enter the second number: '))
if num1 > num2:
    lcm = num1
else:
    lcm = num2
while(True):
    if lcm%num1==0 and lcm%num2==0:
        break
    else:
        lcm = lcm + 1
print('LCM = ',lcm)

num3 = int(input("enter the first number: "))
num4 = int(input('enter the second number: '))
if num3 > num4:
    hcf = num3
else:
    hcf = num4
while(True):
    if num3%hcf==0 and num4%hcf==0:
        break
    else:
        hcf = hcf - 1
print("HCF = ",hcf)
