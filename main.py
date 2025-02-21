from sklearn.datasets import fetch_california_housing # for built in data

df = fetch_california_housing(as_frame=True).frame
# print(df.columns)
# print(df.columns.tolist())

from createFunction import *

create_price_map(df=df, 
                 lat='Latitude', 
                 lng='Longitude', 
                 price='MedHouseVal',
                 size='AveRooms',
                 income='MedInc',
                 filename='California'
                 )