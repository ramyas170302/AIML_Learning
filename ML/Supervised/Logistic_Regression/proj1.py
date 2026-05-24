import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df=pd.read_csv("Students DB.csv")

df["Internet"]=df["Internet"].map(
    {
        "Yes":0,
        "No":1
    }
)

df["SleepQuality"]=df["SleepQuality"].map(
    {
        "Poor":0,
        "Average":1,
        "Good":2,
        "Excellent":3
    }
)
df["Result"]=df["Result"].map(
    {
        "Pass":1,
        "Fail":0
    }
)

x=df[["StudyHours","Attendance","PreviousMarks","Internet","SleepQuality"]]
y=df["Result"]

#spliting
x_train,x_temp,y_train,y_temp=train_test_split(x,y,test_size=0.3,random_state=46)
x_val,x_test,y_val,y_test=train_test_split(x_temp,y_temp,test_size=0.5,random_state=46)

#feature Scaling
scaler=StandardScaler()

x_train=scaler.fit_transform(x_train)
x_val=scaler.transform(x_val)
x_test=scaler.transform(x_test)

model=LogisticRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)


print(f"Accuracy:{accuracy_score(y_test, y_pred)}")
print(f"Confusion Matrix:{confusion_matrix(y_test,y_pred)}")
print(f"Classification Report:")
print(classification_report(y_test,y_pred))

new_student = pd.DataFrame([[7,85,78,0,2]],
    columns=[
        "StudyHours",
        "Attendance",
        "PreviousMarks",
        "Internet",
        "SleepQuality"
    ])
new_student=scaler.transform(new_student)
new_pred=model.predict(new_student)
if new_pred[0]==1:
    print("Pass")
else:
    print("fail")



