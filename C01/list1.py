l=[1,2,3,4,5,6,7,8,9,10]
number=int(input("enter the number: "))
for i in range(len(l)):
    if number==l[i]:
        print("number is present")
        break
else:
     print("number is not present")



