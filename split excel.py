import xlwings as xw

EXCEL_FILE = 'Sample_workbook.xlsx'

try:
    excel_app = xw.APP(visibility=False)
    wb = excel_app.book.open(EXCEL_FILE)
    for sheet in wb.sheets:
        sheet.api.copy()
        wb_new = xw.books.active
        wb_new.save(f'{sheet.name}.xls0x')
        wb_new.close()
finally:
    excel_app.quit()
