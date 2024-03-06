 
# importing pandas 
import pandas as pd 
import glob 
import os 
  
# merging two csv files 
df = pd.concat( 
    map(pd.read_csv, ['acquisition_data.csv', 'layoffs.csv', 'maang_stock_prices_by_quarter.csv']), ignore_index=True) 
print(df) 

file_paths = ['acquisition_data.csv', 'layoffs.csv', 'maang_stock_prices_by_quarter.csv']

  
# Finally, the files are joined 
df = pd.concat(map(pd.read_csv, file_paths), ignore_index=True) 
print(df)

df.to_csv('output_file.csv', index=False)
