
string = str(input("enter the string : "))
new_string = string[-1:] + string[1:-1] + string[:1]
print(new_string)
