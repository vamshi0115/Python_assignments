import pandas as pd

# 1. Define the headers as a list
headers = [
    "Employee ID", "Employee Name", "Age", "Gender", 
    "Department", "Designation", "Date of Joining", 
    "Salary", "Email ID", "Phone Number"
]

# 2. Create an empty DataFrame with these columns
# We use an empty list for data to start with just the headers
df = pd.DataFrame(columns=headers)

# 3. Define the output filename
file_name = "Employee_Data.xlsx"

# 4. Save to Excel
try:
    df.to_excel(file_name, index=False)
    print(f"Successfully created '{file_name}' with 10 column headers.")
except Exception as e:
    print(f"An error occurred: {e}")