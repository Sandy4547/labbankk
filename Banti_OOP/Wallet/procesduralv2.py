def create(amount):
    return {"money": amount}

def check(wallet):
    print(f"The wallet has {wallet['money']} bahts")

def deposit(wallet, amount):
    wallet["money"] += amount

def withdraw(wallet, amount):
    if wallet["money"] >= amount:
        wallet["money"] -= amount
        print(f"Withdraw {amount} bahts successfully")
    else:
        print("Not enough money to withdraw")

# ทดสอบโค้ด
wallet1 = create(1000)    # สร้าง Wallet ที่มียอดเงินเริ่มต้น 1000 บาท
wallet2 = create(2000)    # สร้าง Wallet ที่มียอดเงินเริ่มต้น 2000 บาท

check(wallet1)            # แสดงยอดเงินใน wallet1
check(wallet2)            # แสดงยอดเงินใน wallet2

deposit(wallet1, 500)     # ฝากเงิน 500 บาทใน wallet1
withdraw(wallet2, 1000)   # ถอนเงิน 1000 บาทจาก wallet2

check(wallet1)            # แสดงยอดเงินใน wallet1
check(wallet2)            # แสดงยอดเงินใน wallet2
