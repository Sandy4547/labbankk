# กำหนดค่าเริ่มต้นของยอดเงิน
money = 1000

# ฟังก์ชันสำหรับตรวจสอบยอดเงิน
def check():
    global money
    print(f"ยอดเงินคงเหลือ: {money} บาท")

# ฟังก์ชันสำหรับฝากเงิน
def deposit(amount):
    global money
    money += amount
    print(f"ฝากเงินจำนวน {amount} บาท สำเร็จ")

# ฟังก์ชันสำหรับถอนเงิน
def withdraw(amount):
    global money
    if money >= amount:
        money -= amount
        print(f"ถอนเงินจำนวน {amount} บาท สำเร็จ")
    else:
        print(f"ยอดเงินไม่เพียงพอสำหรับการถอนเงินจำนวน {amount} บาท")

# ทดสอบโค้ด
check()          # แสดงยอดเงินปัจจุบัน
deposit(500)     # ฝากเงิน 500 บาท
check()          # แสดงยอดเงินปัจจุบัน
withdraw(1000)   # ถอนเงิน 1000 บาท
check()          # แสดงยอดเงินปัจจุบัน
