# importing pandas 
import pandas as pd 
import glob 
import os 

df_Acq = pd.read_csv("acq_data.csv")
df_LO = pd.read_csv("layoffs.csv")
df_stock = pd.read_csv("maang_stock_prices_by_quarter.csv")

merge_One = pd.merge(df_Acq, df_LO, on="Company", how="inner")
merged_df = pd.merge(merge_One, df_stock, on="Company", how="inner")
merged_df.to_csv("out.csv", index=False)


df_out = pd.read_csv('out.csv')
# Filter rows where the year is not between 1988 and 2017
df_out = df_out[~df_out['Acquisition Year'].astype(int).between(1988, 2017)]
df_out.to_csv('out2.csv', index=False)

  
# merging two csv files 
# df = pd.concat( 
#     map(pd.read_csv, ['acq_data.csv', 'layoffs.csv', 'maang_stock_prices_by_quarter.csv'])) 
# print(df) 


# # merging the files 
# joined_files = os.path.join("/", "*.csv") 
  
# # A list of all joined files is returned 
# joined_list = glob.glob(joined_files) 
  
# # Finally, the files are joined 
# df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True) 
# print(df)
# df.to_csv("C:/Users/cassi/Desktop/dataMining/dataMining/out.csv", index=False)