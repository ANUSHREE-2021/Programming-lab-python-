string = 'pythonprogramming'
char_freq = {} 
  
for i in string: 
    if i in char_freq: 
        char_freq[i] += 1
    else: 
        char_freq[i] = 1
  

print ("Count of all characters is : " +  str(char_freq)) 