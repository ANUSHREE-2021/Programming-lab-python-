string1=input("enter the first string: ")
string2=input("enter the second string: ")
a=string1[0:1]
string1=string1.replace(string1[0:1],string2[0:1])
string2=string2.replace(string2[0:1],a)
print(string1,string2)