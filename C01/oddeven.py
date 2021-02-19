num = [1,3,43,34,6,22,10,55,45]
even = 0
odd = 0
for i in num:
    if i % 2 == 0:
        even+=1
    else:
        odd+=1
print("even numbers : ",even)
print("odd numbers : ",odd)