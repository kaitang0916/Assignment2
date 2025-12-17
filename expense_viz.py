import csv
import os
import matplotlib.pyplot as plt

# 定義共用的檔案名稱
FILE_NAME = 'expenses.csv'

def load_data():
    """讀取 CSV 並按類別加總金額"""
    category_totals = {}
    
    if not os.path.exists(FILE_NAME):
        print(f"找不到 {FILE_NAME}，請先執行 Member A 的程式來新增資料。")
        return None

    try:
        with open(FILE_NAME, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    category = row['Category']
                    amount = float(row['Amount'])
                    
                    # 累加該類別的金額
                    if category in category_totals:
                        category_totals[category] += amount
                    else:
                        category_totals[category] = amount
                except ValueError:
                    continue # 跳過資料損毀的行
        return category_totals
    except Exception as e:
        print(f"讀取錯誤: {e}")
        return None

def generate_pie_chart(data):
    """根據數據繪製圓餅圖"""
    if not data:
        print("沒有足夠的資料可以繪圖。")
        return

    labels = list(data.keys())
    sizes = list(data.values())

    # 設定中文字型 (避免亂碼，視系統而定，這裡是通用設定)
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial Unicode MS', 'SimHei'] 
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Expense Distribution by Category')
    plt.axis('equal') # 讓圓餅圖保持圓形
    plt.show()

if __name__ == "__main__":
    print("=== Member B: 產生圓餅圖 ===")
    data = load_data()
    if data:
        print(f"讀取到的數據: {data}")
        generate_pie_chart(data)