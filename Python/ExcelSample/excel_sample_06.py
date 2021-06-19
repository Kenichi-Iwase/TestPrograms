from openpyxl import Workbook

# 指定した数だけワークブックを作成するスクリプト

# 作成するブック数を入力
count = input('作成するブック数：　')

# ワークブックを作成する
for i in range(int(count)):
    wb = Workbook()
    ws = wb.active
    ws.title = '概要'
    wb.save(f'資料_{i+1}.xlsx')
