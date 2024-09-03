#import csv library
import csv

income = 0
#open the csv file
with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file)
  #reads contents of csv file into 'reader' variable 
  for row in reader:
    income += float(row["Quantity"]) * float(row["Cost"])
print("My Shop Income Tracker $$$")
print(f"Your shop earned a Total income of : ${round(income,2)} today")




