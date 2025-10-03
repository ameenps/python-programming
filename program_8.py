#Create a string from a given string where the first and last characters are exchanged.

s = input("enter a word ")
print(f"modified : {s[-1 ]+ s[1:-1] + s[0] }")