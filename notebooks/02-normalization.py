# importing libraries
import pandas as pd

# load the csv file
file = './output/us-shein-clean-products.csv'
goods_df = pd.read_csv(file)

# check if the data frame is in its desired format

# print(df.head())
# print(df.columns)
# print(df.shape)
# print(df.info())
# print(df.describe())

# normalize into relational tables
category_df = goods_df[['category']].drop_duplicates()

category_df = category_df.reset_index(drop=True)
category_df['category-id'] = category_df.index + 1

# merges the two dfs adding the category id next to its correspondant category
goods_df = goods_df.merge(category_df, on='category')

# delete the category name and keep it's id
goods_df = goods_df.drop(columns= 'category')

# save to clean csvs

category_df.to_csv('./output/us-shein-categories.csv', index=False)
goods_df.to_csv('./output/us-shein-goods.csv', index=False)