
import pandas as pd

Emp = pd.read_csv('employees.csv')
# Loaded employees csv into a pandas dataframe
E = Emp[Emp['employee_type'] == "Manager"]
# Filtered the employees Dataframe based on employee type
Avg = E['salary'].mean()
# Average of Manager group employee_type
Low_Salary = Emp['salary'].min()
print(Low_Salary)

Low_Salary_Record = Emp[Emp['salary'] == Low_Salary]
#  Details of the lowest salaried employee
