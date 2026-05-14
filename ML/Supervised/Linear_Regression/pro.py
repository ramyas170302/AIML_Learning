import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error

df=pd.read_csv("Linear_Regression.csv")

df["Gender"]=df["Gender"].map(
    {
        "Male":0,
        "Female":1
    }
)
df["Internet"]=df["Internet"].map(
    {
        "Yes":0,
        "No":1
    }
)
df["Department"]=df["Department"].map(
    {
        "CSE":1,
        "ISE":0,
        "ECE":2,
        "ME":3
    }
)

df["SleepQuality"]=df["SleepQuality"].map(
    {
        "Poor":0,
        "Average":1,
        "Good":1,
        "Excellent":3    
    }
)

df["AssignmentLevel"]=df["AssignmentLevel"].map(
    {
        "Low":0,
        "Medium":1,
        "High":2
    }
)

x=df[["StudyHours","Attendance","Internet","PreviousMarks","SleepQuality","AssignmentLevel"]]
y=df["FinalMarks"]

x_train,x_temp,y_train,y_temp=train_test_split(x,y,test_size=0.3,random_state=46)

x_val,x_test,y_val,y_test=train_test_split(x_temp,y_temp,test_size=0.5,random_state=46)

scaler_model=StandardScaler()

# feature scaling
x_train=scaler_model.fit_transform(x_train)

x_val=scaler_model.transform(x_val)

x_test=scaler_model.transform(x_test)


model=LinearRegression()

model.fit(x_train,y_train)

y_pred=model.predict(x_test)

mse=mean_squared_error(y_test,y_pred)

print(mse)

r2=r2_score(y_test,y_pred)

print(r2)