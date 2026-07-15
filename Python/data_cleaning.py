import pandas as pd
df = pd.read_csv("Dataset\Amazon Sale Report.csv")
print("Data set loaded Successfull")
print("Dataset Shape:", df.shape)

print(df.head())

print(df.dtypes)

print(df.isnull().sum())

df.duplicated().sum()
#convert amount to numeric
df["Amount"] = pd.to_numeric(df["Amount"],
errors="coerce"
)

#Replace missing amount values with 0

df["Amount"]= df["Amount"].fillna(0)

#Remove duplicate rows
df = df.drop_duplicates()

#save cleaned data 
df.to_csv("Dataset/Amazon_Sales_Cleaned.csv", index=False)

print("Shape:", df.shape)
print("Missing Amount:",
      df["Amount"].isnull().sum())

