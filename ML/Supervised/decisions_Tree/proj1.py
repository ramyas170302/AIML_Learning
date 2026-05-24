import pandas as pd
from sklearn.preprocessing import LabelEncoder 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error,r2_score


df=pd.read_csv("Loan.csv")

# check for null values
print(df.isnull().sum())

# remove all the null values with mean values 
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["CreditScore"]=df["CreditScore"].fillna(df["CreditScore"].mean())
df["Experience"]=df["Experience"].fillna(df["Experience"].mean())

#after checks of null sum
print(df.isnull().sum())

#Decoding
encoder=LabelEncoder()
df["ExistingLoan"]=encoder.fit_transform(df["ExistingLoan"])  # yes-1    No-0
df["JobType"]=encoder.fit_transform(df["JobType"])
df["Property"]=encoder.fit_transform(df["Property"])
df["LoanStatus"]=encoder.fit_transform(df["LoanStatus"])
print(df)

# Feature and Labels
x=df[["Age","Salary","CreditScore","ExistingLoan","JobType","Experience","Property"]]
y=df["LoanStatus"]

#spliting
x_train,x_temp,y_train,y_temp=train_test_split(x,y)
x_val,x_test,y_val,y_test=train_test_split(x_temp,y_temp)

model=DecisionTreeClassifier()

model.fit(x_train,y_train)
y_pred=model.predict(x_test)

print(mean_squared_error(y_test,y_pred))
print(r2_score(y_test,y_pred))







