dict = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30, 'july': 31, 'august': 31,'september': 30, 'october': 31, 'november': 30, 'december': 31}
month = input("enter a month : ")
print("number of days in", month, "=" ,dict[month])
print(sorted(dict.keys()))
for i in dict:
    if dict [i]== 30:
        print(i)
    