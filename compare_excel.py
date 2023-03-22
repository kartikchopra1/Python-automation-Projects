from pathlib import Path
import pandas as pd
import xlwings as xw

initial_version = Path.cwd() / "Same_Shape" / "Arrival_Dates.xlsx"
updated_version = Path.cwd() / "Same_Shape" / "Arrival_Dates_Finals.xlsx"

df_initial = pd.read_excel(initial_version)
df_initial.head(3)

df_update = pd.read_excel(updated_version)
df_update.head(3)

df_initial.shape
df_update.shape
df_initial.shape == df_update.shape

diff = df_update.compare(df_initial, align_axis=1)
diff

diff = df_update.compare(df_initial, keep_shape=True, keep_equal=False)
diff

diff = df_update.compare(df_initial, align_axis=1)
diff.to_excel(Path.cwd() / "Same_Shape" / "Difference.xlsx")

# highlight the differences

with xw.App(visible=False) as app:
    initial_wb = app.books.open(initial_version)
    initial_ws = initial_wb.sheets(1)

    updated_wb = app.books.open(updated_version)
    updated_ws = updated_wb.sheets(1)

    for cell in updated_ws.used_range:
        old_value = initial_ws.range((cell.row, cell.column)).value
        if cell.value != old_value:
            # WARNING: Platform specific (!)
            cell.api.AddComment(f"Value from {initial_wb.name}: {old_value}")
            cell.color = (255, 71, 76)  # light red

    updated_wb.save(Path.cwd() / "Same_Shape" / "Difference_Highlighted.xlsx")

# highlight the different  numebr of rows
initial_version = Path.cwd() / "Different_Shape" / "Arrival_Dates.xlsx"
updated_version = Path.cwd() / "Different_Shape" / "Arrival_Dates_Final.xlsx"

df_initial = pd.read_excel(initial_version)
df_initial.shape

df_update = pd.read_excel(updated_version)
df_update.shape

df_initial.shape == df_update.shape

# We need the index information to highlight the rows in Excel
df_update = df_update.reset_index()
df_update.head(3)

# Merge dataframes and add inidactor column
df_diff = pd.merge(df_initial, df_update, how="outer", indicator="Exist")
df_diff

# Show only the differnce
df_diff = df_diff.query("Exist != 'both'")
df_diff

# Show only the data we want to highlight
df_highlight = df_diff.query("Exist == 'right_only'")
df_highlight

# Get the row numbers we want to highlight in Excel
highlight_rows = df_highlight['index'].tolist()
highlight_rows

# Convert floats to integers
highlight_rows = [int(row) for row in highlight_rows]
highlight_rows

# pandas index starts at 0
# Excel data (w/o header) starts from row 2
first_row_in_excel = 2

highlight_rows = [x + first_row_in_excel for x in highlight_rows]
highlight_rows

# Highlight the rows in Excel
with xw.App(visible=False) as app:
    updated_wb = app.books.open(updated_version)
    updated_ws = updated_wb.sheets(1)
    rng = updated_ws.used_range

    print(f"Used Range: {rng.address}")

    # Hightlight the rows in Excel
    for row in rng.rows:
        if row.row in highlight_rows:
            row.color = (255, 71, 76)  # light red

    updated_wb.save(Path.cwd() / "Different_Shape" / "Difference_Highlighted.xlsx")
