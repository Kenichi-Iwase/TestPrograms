import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# 売上データ(CSV)をExcelファイルに出力するスクリプト

book = Workbook()
sheet = book.active

data_frame = pd.read_csv('uriage.csv', encoding='utf-8')

for row in dataframe_to_rows(data_frame, index=None, header=True):
    sheet.append(row)

book.save('売上高.xlsx')
