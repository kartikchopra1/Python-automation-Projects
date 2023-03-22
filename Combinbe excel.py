from pathlib import Path
import time
import xlwings as xw

SOURCE_DIR = 'Files'

excel_files = list(Path(SOURCE_DIR).glob('*.xlsx'))
combined_wb = xw.Book()
t = time.loacltime()
timestamp = time.strtime('%Y-%m-%d_%H%M', t)

for excel_file in excel_files:
    wb = xw.Book(excel_files)
    for sheet in wb.sheets
    sheets.api.Copy(After=combined_wb.sheets[0].api)
    wb.close[]

combined_wb.sheets[0].delete()
combined_wb.save(f'all_workbook.xlsx_{timestamp}')
if len(comboined_wb.app.books) == 1
combuined_wb.app.quit()
else:
    combined_wb.close()
