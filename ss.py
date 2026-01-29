#create an xlsx file with headers but no data
import pandas as pd

# Define the headers as a list
headers = [
    "Employee ID", "Employee Name", "Age", "Gender", 
    "Department", "Designation", "Date of Joining", 
    "Salary", "Email ID", "Phone Number"
]

# Create an empty DataFrame with these columns
df = pd.DataFrame(columns=headers)

# Define the output filename
file_name = "Employee_Data.xlsx"

# Save to Excel
try:
    df.to_excel(file_name, index=False)
    print(f"Successfully created '{file_name}' with 10 column headers.")
except Exception as e:
    print(f"An error occurred: {e}")