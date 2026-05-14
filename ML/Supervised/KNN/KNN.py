import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

df=pd.read_csv("Stdents.csv")

#print(df)

df["Gender"]=df["Gender"].map({
    "Male":0,
    "Female":1
})

df["Internet"]=df["Internet"].map({
    "Yes":1,
    "No":0
})

df["Result"]=df["Result"].map({
    "Pass":1,
    "Fail":0
})
#print(df)

x=df[["StudyHours","Attendance","Gender","Internet","PreviousMarks"]]
y=df["Result"]

# first split:

x_train,x_temp,y_train,y_temp=train_test_split(x,y,test_size=0.3,random_state=42)

# second split

x_val,x_test,y_val,y_test=train_test_split(x_temp,y_temp,test_size=0.5,random_state=42)


scaler=StandardScaler()

x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)
#using KNN:
# low k value more accuracy.
model=KNeighborsClassifier(n_neighbors=2)

model.fit(x_train,y_train)

y_pred=model.predict(x_test)

print(accuracy_score(y_test, y_pred))

