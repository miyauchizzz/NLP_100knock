def conversion(str1):
    result = ""
    for i in str1:
        if i.islower():
            result += chr(219 - ord(i))
    
        else:
            result += i
    return result 

str1 = "I like apple"
text = conversion(str1)
print(text)
print(conversion(text))
