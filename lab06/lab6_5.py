import matplotlib.pyplot as plt
import codecs

# อ่านข้อมูลจากไฟล์ points.txt
file_path = 'C:/Users/panna/OneDrive/code/Lab6/points.txt'  # ระบุเส้นทางไปยังไฟล์ points.txt

# อ่านข้อมูลและแยกค่าพิกัด x และ y
xs = []
ys = []
with codecs.open(file_path, 'r', encoding='utf-8-sig') as file:  # เปิดไฟล์ด้วย utf-8-sig เพื่อตัด BOM
    for line in file:
        try:
            x, y = map(float, line.strip().split(','))  # แปลงเป็น float แทน int
            xs.append(x)
            ys.append(y)
        except ValueError:
            print(f"บรรทัดที่ไม่สามารถแปลงได้: {line.strip()}")  # แจ้งเตือนเมื่อข้อมูลแปลงไม่ได้

# สร้างกราฟ
plt.scatter(xs, ys, color='red')  # ใช้ scatter plot และกำหนดให้จุดมีสีแดง
plt.xlabel('X')  # กำหนด label แกน X
plt.ylabel('Y')  # กำหนด label แกน Y
plt.title('Scatter Plot from points.txt')  # กำหนดหัวข้อกราฟ
plt.grid(True)  # เพิ่มตารางในกราฟ

# แสดงกราฟ
plt.show()
