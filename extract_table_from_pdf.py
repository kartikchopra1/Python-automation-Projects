import camelot

tables = camelot.read_pdf('foo.odf', pages='1')
print(tables)

tables.export('foo.csv', f='csv', compress=True)
tables[0]
