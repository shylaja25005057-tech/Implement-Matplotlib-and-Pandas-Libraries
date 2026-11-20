# Implement Matplotlib and Pandas

import pandas as pd
import matplotlib.pyplot as plt

# Create Student Dataset

data = {
    "Name": ["Arun", "Bala", "Charan", "Divya",
             "Esha", "Farhan", "Geeta", "Hari"],

    "Marks": [65, 72, 90, 65, 78, 88, 95, 70],

    "Attendance": [90, 85, 95, 75, 80, 92, 98, 78]
}

df = pd.DataFrame(data)

# Display Dataset
print("Student Dataset:")
print(df)

# 1. Bar Chart
plt.figure()
plt.bar(df["Name"], df["Marks"])
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Marks - Bar Chart")
plt.show()

# 2. Line Chart
plt.figure()
plt.plot(df["Name"], df["Marks"], marker="o")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Marks - Line Chart")
plt.show()

# 3. Pie Chart
plt.figure()
plt.pie(df["Marks"], labels=df["Name"], autopct="%1.1f%%")
plt.title("Student Marks - Pie Chart")
plt.show()
