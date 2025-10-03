#Get a string from an input string
#  where all occurrences of the first character are replaced with '$' 
#  except the first character. eg: onion - oni$n

string = input("enter a word :")
first = string[0]
replace = string.replace(string[0] ,'$' )
result = first + replace[1:]
print(result)