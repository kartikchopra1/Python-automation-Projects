import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('melb_data.csv')
profile = ProfileReport(df, title='EDA Houseperices')
profile.to_file('EDA_Housepercise_Analysis.html')

# Read Excel File
# df = pd.read_excel('YOURFILENAME.xlsx', sheet_name='Sheet1')
