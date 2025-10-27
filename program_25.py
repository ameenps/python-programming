def countChar(inputString): 
    Count = {} 
    for i in inputString: 
        if i in Count: 
            Count[i] += 1 
        else: 
            Count[i] = 1 
    return Count 
str2 = input("Enter a string: ") 
result = countChar(str2) 
print(result)