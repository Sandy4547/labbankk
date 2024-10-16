import pandas as pd
import os
import sys
import io

# Set the standard output encoding to utf-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def read_distance_matrix(file_path):
    """อ่านตารางระยะทางจากไฟล์ CSV และแปลงเป็น DataFrame"""
    if not os.path.isfile(file_path):
        print(f"ไม่พบไฟล์ที่ตำแหน่ง: {file_path}")
        return None

    try:
        df = pd.read_csv(file_path, header=None)
        return df
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการอ่านไฟล์: {e}")
        return None


def calculate_total_distance(df, points):
    """คำนวณระยะทางรวมตามลำดับสถานที่ที่กำหนด"""
    total_distance = 0
    for i in range(len(points) - 1):
        start = points[i]
        end = points[i + 1]
        total_distance += df.iloc[start, end]

    return total_distance


def main():
    current_path = os.getcwd()
    file_path = os.path.join(current_path, "Lab6", "DM.csv")

    df = read_distance_matrix(file_path)
    if df is not None:
        points = [7, 8, 9]
        total_distance = calculate_total_distance(df, points)
        print(f"ระยะทางรวมจาก T8 ไป T9 ไป T10: {total_distance} หน่วย")


if _name_ == "_main_":
    print("\n####################################\n")
    main()
    print("\n####################################\n")