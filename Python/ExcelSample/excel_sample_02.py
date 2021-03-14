# Load Excel workbook and write data
import openpyxl
book = openpyxl.load_workbook('catalog.xlsx')
sheet = book.active
sheet['A1'] = 'hat'
sheet['B1'] = 2000
book.save('catalog.xlsx')
