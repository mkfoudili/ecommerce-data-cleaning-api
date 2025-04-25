import pandas as pd
from sqlalchemy import create_engine

# option : 01 :
# creating a simple table schema using mysql alchemy (no primary / foreign keys / no constraints)

engine = create_engine('mysql+pymysql://root:root@localhost:3306/us_shein_products')

goods_file = './output/us-shein-goods.csv'
category_file = './output/us-shein-categories.csv'

goods_df = pd.read_csv(goods_file)
category_df = pd.read_csv(category_file)


# Creating tables
goods_df.to_sql('goods', con=engine, if_exists='replace', index=False)
category_df.to_sql('categories', con=engine, if_exists='replace', index=False)