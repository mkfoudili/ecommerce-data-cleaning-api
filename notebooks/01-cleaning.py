# importing libraries
import pandas as pd
import numpy as np
import re
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


# some functions to explore the data frame

# print(df.head())
# print(df.columns)
# print(df.shape)
# print(df.info())
# print(df.describe())

# how many missing values de we have in each column ?
# print(df.isnull().sum())

# pourcentage of null in each column
# total_missing = df.isnull().sum()

# total_cells = df.size
# # or: total_cells = np.product(df.shape)

# print((total_missing/total_cells) * 100)

# handeling missing values
# 01- discount
df['discount'] = df['discount'].fillna(0)

# 02- price
mod = df.groupby('category')['price'].agg(lambda x: x.mode().iloc[0])
df['price'] = df['price'].fillna(df['category'].map(mod))

# 03- rank title / rank sub
df['rank-title'] = df['rank-title'].fillna('')
df['rank-sub'] = df['rank-sub'].fillna('')

# 04- product color
df['color-count'] = df['color-count'].fillna(0)

# 06- selling proposition
df['selling_proposition'] = df['selling_proposition'].fillna('')

# 07- product title
df['goods-title-link--jump'] = df['goods-title-link--jump'].fillna('')
df['goods-title-link'] = df['goods-title-link'].fillna('')

# handeling empty columns
df['goods-title'] = df['goods-title-link']
df[df['goods-title'] == '' 'goods-title'] = df['goods-title-link--jump']

# drop unnecessary columns (duplicates, irrelevent to the analysis)
df = df.drop('goods-title-link--jump', axis=1)
df = df.drop('goods-title-link--jump href', axis=1)
df = df.drop('goods-title-link', axis=1)
df = df.drop('blackfridaybelts-bg src', axis=1)
df = df.drop('blackfridaybelts-content', axis=1)
df = df.drop('product-locatelabels-img src', axis=1)

# print data after handeling null values
# print(df.isnull().sum())

# satndarisation
# 01- clean column names
df.columns = df.columns.str.replace('_','-')
df.columns = df.columns.str.replace(' ','-')

# 02- lower / upper case
df['goods-title'] = df['goods-title'].str.title()
df['category'] = df['category'].str.title()
df['category'] = df['category'].str.replace('_',' ')
df['selling-proposition'] = df['selling-proposition'].str.title()
df['rank-title'] = df['rank-title'].str.title()
df['rank-sub'] = df['rank-sub'].str.title()

# 03- trim white spaces
for column in df.columns:
    if df[column].dtype == object:
        df[column] = df[column].str.split().str.join(' ')

# 04- trating inconsistent data entries
# use value counts on each column to find inconsistencies

# print(df['category'].value_counts())
# print(df['color-count'].value_counts())
# print(df['discount'].value_counts())
# print(df['goods-title'].value_counts())
# print(df['price'].value_counts())
# print(df['rank-sub'].value_counts())
# print(df['rank-title'].value_counts())
# print(df['selling-proposition'].value_counts())

ranks = []
for rank in df['rank-title']:
    if 'Sellers' in rank:
        rank = rank.replace('Sellers','Seller')    
    ranks.append(rank)

df['rank-title'] = ranks

# verify the format of this column
pattern = r"^\d+(\.\d+)?K?\+\sSold Recently$"

# for prop in df['selling-proposition']:
#     if not re.match(pattern, prop) and prop != '':
#         # print(prop)
