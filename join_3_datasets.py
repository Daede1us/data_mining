 
# importing pandas 
import pandas as pd 
import glob 
import os 
  
# merging two csv files 
df = pd.concat( 
    map(pd.read_csv, ['mydata.csv', 'mydata1.csv']), ignore_index=True) 
print(df) 


# merging the files 
joined_files = os.path.join("/home", "mydata*.csv") 
  
# A list of all joined files is returned 
joined_list = glob.glob(joined_files) 
  
# Finally, the files are joined 
df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True) 
print(df)