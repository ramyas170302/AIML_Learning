import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
import numpy as np



#load csv database
df = pd.read_csv("ML/Supervised/Mini_ML_Proj/DataBase.csv")



#encoding
encoder=LabelEncoder()
df["StressLevel"]=encoder.fit_transform(df["StressLevel"])
df["SocialInteraction"]=encoder.fit_transform(df["SocialInteraction"])

df["MentalHealthRisk"]=df["MentalHealthRisk"].map(
    {
        "Low Risk":0,
        "Medium Risk":1,
        "High Risk":2
    }
)


#feature,label
x=df[["SleepHours","StressLevel","ScreenTime","ExerciseHours","SocialInteraction","WaterIntake","WorkPressure"]]
y=df["MentalHealthRisk"]

#Model creation
model = DecisionTreeClassifier(
    max_depth=4,              # slightly deeper than 3
    min_samples_split=10,     # prevents overfitting
    min_samples_leaf=5,       # very important improvement
    random_state=42
)

#spliting
x_train,x_temp,y_train,y_temp=train_test_split(x,y,test_size=0.2,random_state=46)
x_val,x_test,y_val,y_test=train_test_split(x_temp,y_temp,test_size=0.5,random_state=46)

#learn
model.fit(x_train,y_train)

#Prediction 
y_pred=model.predict(x_test)

#metrics
ac=accuracy_score(y_test,y_pred)
print(f"Accuracy : {ac}")
cm=confusion_matrix(y_test,y_pred)
print(cm)

    






