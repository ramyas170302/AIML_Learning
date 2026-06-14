import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix,accuracy_score,f1_score,recall_score

df=pd.read_csv("heart.csv")

print(df.head())
print(df.isnull().sum())
df.info()
print(df.columns)

#feature,label
x=df[["age","sex","cp", "trestbps", "chol", "fbs", "restecg", "thalach","exang", "oldpeak", "slope", "ca", "thal"]]
y=df["target"]

#split
x_train,x_temp,y_train,y_temp=train_test_split(x,y,train_size=0.7,random_state=46)
x_val,x_test,y_val,y_test=train_test_split(x_temp,y_temp,test_size=0.5,random_state=46)

#standard scaler
scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)

#model

model=SVC()
model.fit(x_train,y_train)

#pred=model.predict(x_test)




#metrics

'''cm=confusion_matrix(y_test,pred)
print(cm)
print(accuracy_score(y_test,pred))
print(f1_score(y_test,pred))
print(recall_score(y_test,pred))'''


#new data test
new_data = [[63,1,3,145,233,1,0,150,0,2.3,0,0,1]]
pred=model.predict(new_data)
if pred==0:
    print("No heart Disease")
else:
    print("Heart disease ")
