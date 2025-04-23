# importing libraries
import pandas as pd
import os

# load csv files
folder = './data'
df_list = []
df = pd.DataFrame()


for csv_file in os.listdir(folder):
    file = os.path.join(folder,csv_file)
    df = pd.read_csv(file)
    # every csv file is a product category so add this as a column
    category = csv_file.split('-')[-2]
    df['category'] = category
    df_list.append(df)

# merge all csv files
df = pd.concat(df_list, ignore_index=True)

# print(df.head())
# print(df.columns)
# print(df.shape)
# print(df.info())
# print(df.describe())