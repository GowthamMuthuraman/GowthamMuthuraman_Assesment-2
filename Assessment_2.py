
import pandas as pd

Emp = pd.read_csv('employees.csv')
# Loaded employees csv into a pandas dataframe
E = Emp[Emp['employee_type'] == "Manager"]
# Filtered the employees Dataframe based on employee type
Avg = E['salary'].mean().astype(int)
# Average of Manager group employee_type
Low_Salary = Emp['salary'].min()
Low_Salary_Record = Emp[Emp['salary'] == Low_Salary]
#  Details of the lowest salaried employee

First_name = Low_Salary_Record['first_name'].item()
Last_name = Low_Salary_Record['last_name'].item()

print("Average Salary of Manager group:", Avg)
print(First_name,Last_name, "has the lowest salary")