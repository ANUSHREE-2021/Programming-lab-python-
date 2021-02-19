#list
list_1 = [1,2,3,4]
list_2 = [12,24,5,6]
if len(list_1) == len(list_2):
    print("length is same")
else:
    print("length is not same")
sum=0
for x in list_1:
    sum=sum+x
    
sum1=0
for y in list_2:
    sum1=sum1+y
    
if sum==sum1:
    print("sum is same")
else:
    print("sum is not same")
flag=0
for x in list_1:
    if x in list_2:
        flag=1
if flag==1:
  print(True)
else:
    print(False)
