import matplotlib.pyplot as plt

# กำหนดค่าพิกัด x และ y
xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ys = [4, 8, 5, 6, 8, 2, 1, 4, 3, 1]

# สร้างกราฟ
plt.scatter(xs, ys, color='red')  # ใช้ scatter plot และกำหนดให้จุดมีสีแดง
plt.xlabel('X')  # กำหนด label แกน X
plt.ylabel('Y')  # กำหนด label แกน Y
plt.title('Scatter Plot of Given X and Y Coordinates')  # กำหนดหัวข้อกราฟ

# แสดงกราฟ
plt.show()