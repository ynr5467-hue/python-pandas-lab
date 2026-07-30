import pandas as pd

data = """Roll-No\tName\tDepartment\tPercentage
101\tHarshi\tIT\t89
102\tPrathibha\tIT\t92
103\tGeetha\tCSE\t88
104\tSeetha\tECE\t85"""

with open("students.txt", "w") as f:
    f.write(data)

df = pd.read_csv("students.txt", sep="\t")
print("Student data:")
print(df)

df = pd.read_table("students.txt")
print(df)
