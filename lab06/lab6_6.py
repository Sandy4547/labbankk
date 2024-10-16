import pandas as pd

# อ่านข้อมูลจากไฟล์ travel.csv
file_path = 'C:/Users/panna/OneDrive/code/Lab6/travel.csv'  # ระบุเส้นทางไปยังไฟล์ travel.csv

# อ่านข้อมูลจากไฟล์ CSV
data = pd.read_csv(file_path)


print(data)


print(data.head())


print(data.tail())


print(data.describe())