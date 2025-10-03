#Enter two list of integers. 
# Check: a. Whether list are of the same length 
# b. whether list sums to same value 
# c. whether any value occurs in both

#a. Whether list are of the same length 

list1 = [1,2,3,45,55,55,6,77,77]
list2 = [1,2,34,45,66,77,44,22]
print(len(list1))
print(len(list2))

if len(list1) == len(list2):
    print("both list has same length")
else:
    print("both list has different length")

# b. whether list sums to same value 

print(f"""sum of list 1 :  {sum(list1)} 
sum of list 2 :  {sum(list2)}""")

if sum(list1) == sum(list2):
    print("both list has same total number of values")
else:
    print("both list has different total number of values")

# c. whether any value occurs in both

common_values =  set(list1) & set(list2)
print("common valuse are : ",common_values)

