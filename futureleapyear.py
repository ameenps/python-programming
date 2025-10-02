
import datetime

current_year = datetime.date.today().year
final_year = int(input("enter the final year"))
if current_year > final_year :
    print("end year must be greater than starting year")
else:
    print(f"leap years from {current_year}to{final_year}:")

for year in range(current_year,final_year+1):
    if(year % 4 == 0 and year % 100!=0):
        print(year)