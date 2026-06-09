import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
#from sklearn.metrics import confusion_matrix,f1_score,accuracy_score

df=pd.read_csv("loan_approval_dataset.csv")

df.columns = df.columns.str.strip()
df.drop("loan_id",axis=1,inplace=True)
#encode

encode=LabelEncoder()
df["education"]=df["education"].map({
    "Graduate":1,
    "Not Graduate":0
})
df["self_employed"]=df["self_employed"].map({
    "Yes":1,
    "No":0
})
df["loan_status"] = df["loan_status"].str.strip()
df["loan_status"]=df["loan_status"].map({
   "Approved":1,
   "Rejected":0
})

#feature ,label
x=df[["no_of_dependents","education","self_employed","income_annum","loan_amount","loan_term","cibil_score","residential_assets_value","commercial_assets_value","luxury_assets_value","bank_asset_value"]]
y=df["loan_status"]

#split
x_train,x_temp,y_train,y_temp=train_test_split(x,y,random_state=46,train_size=0.7)
x_test,x_val,y_test,y_val=train_test_split(x_temp,y_temp,test_size=0.5)

#model creation
model=RandomForestClassifier(n_estimators=100,max_depth=5,random_state=46,min_samples_leaf=2)
model.fit(x_train,y_train)

#predict=model.predict(x_test)

#metrics
'''ac=accuracy_score(y_test,predict)
print(ac)
cm=confusion_matrix(y_test,predict)
print(cm)
f1=f1_score(y_test,predict)
print(f1)'''

# to check overfit or underfit:
'''train_acc = model.score(x_train,y_train)
test_acc = model.score(x_test,y_test)

print(train_acc)
print(test_acc)'''




