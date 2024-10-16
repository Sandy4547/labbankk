import pandas as pd
import matplotlib.pyplot as plt

# อ่านข้อมูลจากไฟล์ CSV
df = pd.read_csv('C:/Users/panna/OneDrive/code/Lab6/travel.csv')

# สร้างกราฟ
plt.figure(figsize=(8, 6))
plt.scatter(df['Lat'], df['Lng'], c='blue', label='Locations')

# แสดงตำแหน่ง T1-T10
for i in range(len(df)):
    plt.annotate(f'T{i+1}', (df['Lat'][i], df['Lng'][i]), textcoords="offset points", xytext=(0,10), ha='center')

# กำหนดชื่อแกนและหัวเรื่อง
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('Tourist Locations')
plt.legend()
plt.grid(True)

# แสดงกราฟ
plt.show()