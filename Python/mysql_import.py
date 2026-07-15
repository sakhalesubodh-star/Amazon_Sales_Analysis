import  pandas as pd 
from sqlalchemy import create_engine

df=pd.read_csv("Dataset/Amazon_Sales_Cleaned.csv")

df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_")
    .str.replace("-", "_")
    .str.replace(":", "")
)

engine = create_engine(
    "mysql+pymysql://root:rootpassword@localhost:3306/ecommerce_analysis"
)

df.to_sql("amazon_sales", con=engine,
          if_exists="replace",
          index=False 
          )
print("Data imported succecfully in mysql")
