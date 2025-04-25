import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, String, Float, ForeignKey, MetaData

# option : 02 :
# creating a tables with proper constraints / primary / stranger keys
engine = create_engine('mysql+pymysql://root:root@localhost:3306/us_shein_products')

goods_file = './output/us-shein-goods.csv'
category_file = './output/us-shein-categories.csv'

goods_df = pd.read_csv(goods_file)
category_df = pd.read_csv(category_file)

metadata = MetaData()

categories = Table('categories', metadata,
    Column('category-id', Integer, primary_key=True),
    Column('category', String)
)

goods = Table('goods', metadata,
    Column('goods-id', Integer, primary_key=True),
    Column('goods-title', String),
    Column('price', Float),
    Column('discount', Integer),
    Column('color-count', Float),
    Column('rank-title', Integer),
    Column('rank-sub', String),
    Column('selling-proposition', Float),
    Column('category-id', Integer, ForeignKey('categories.category-id'))
)

metadata.create_all(engine)

category_df.to_sql('categories', con=engine, if_exists='append', index=False)
goods_df.to_sql('goods', con=engine, if_exists='append', index=False)