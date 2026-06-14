import pandas as pd

df=pd.read_csv("Mall_Customers.csv")



df["Gender"]=df["Gender"].map({
    "Male":0,
    "Female":1
})

print(df.head())