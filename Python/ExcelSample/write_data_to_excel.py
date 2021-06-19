from openpyxl import Workbook

# Excelにデータを出力するスクリプト

book = Workbook()
sheet = book.active
sheet['A1'] = 'Hello world!'
sheet['A2'] = 'こんにちは。'
sheet['A3'] = '2021/6/19'
sheet['A4'] = 'Side 3'
sheet['A5'] = 3
sheet['A6'] = 1.41421356
sheet['A7'] = 'Yet the earth moves around the sun.'
book.save('TestBook.xlsx')
