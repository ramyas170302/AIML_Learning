import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as pt
import math 

df=pd.read_csv("Mall_Customers.csv")


'''print(df.head())
print(df.info())
print(df.isnull().sum())
'''
df.rename(columns={
    "Annual Income (k$)": "Income",
    "Spending Score (1-100)": "Spending_Score"
}, inplace=True)

x=df[["Income","Spending_Score"]]
df.drop(["CustomerID", "Age", "Gender"], axis=1, inplace=True)


# to check elbow point:
'''k=[]
for i in range (1,11):
    model=KMeans(n_clusters=i)
    model.fit(x)
    print(i,model.inertia_)
    k.append(model.inertia_)
    


pt.scatter(range(1,11),k)
pt.show()'''


'''y=pd.DataFrame({
    "Income":[20],
    "Spending_Score":[18]
    })'''
model=KMeans(n_clusters=4)
model.fit(x)
cluster=model.predict(x)
df["Cluster"]=cluster
#print(df)
print(cluster)

print(df.groupby("Cluster").mean())

cluster_group={
    0:"Low Income Customer",
    1:"Middle Income Customer",
    2:"High Income,Low Spending",
    3:"High Income,High Spending"
}

df["Cluster_group"]=df["Cluster"].map(cluster_group)
print(df)

