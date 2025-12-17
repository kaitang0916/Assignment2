import csv
import os
from datetime import datetime

# 定義共用的檔案名稱
FILE_NAME = 'expenses.csv'

def initialize_file():
    """初始化檔案：如果檔案不存在，則建立並寫入標題"""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Amount', 'Category', 'Description'])

def add_expense():
    print("\n=== Member A: 新增支出 ===")
    
    # 1. 日期 (預設今天)
    date_input = input("日期 (YYYY-MM-DD, 按 Enter 為今天): ")
    if not date_input:
        date_input = datetime.now().strftime("%Y-%m-%d")
    
    # 2. 金額 (驗證數字)
    while True:
        try:
            amount = float(input("金額: "))
            break
        except ValueError:
            print("錯誤: 請輸入有效的數字")

    # 3. 類別
    category = input("類別 (例如: 食物, 交通, 娛樂): ")
    
    # 4. 備註
    note = input("備註 (可選): ")

    # 寫入 CSV
    try:
        with open(FILE_NAME, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([date_input, amount, category, note])
        print(f"✅ 已儲存: {category} ${amount}")
    except Exception as e:
        print(f"❌ 寫入錯誤: {e}")

if __name__ == "__main__":
    initialize_file()
    while True:
        add_expense()
        if input("繼續新增? (y/n): ").lower() != 'y':
            break