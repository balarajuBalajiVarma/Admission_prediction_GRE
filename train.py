import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.helper import Readdata,missing_treatment,drop_const_var,splitdata,train_test_split
from sklearn.linear_model import LinearRegression

#Calling pyscrips from helper
df=Readdata()

missing_treated_df=missing_treatment(df)

drop_const_df=drop_const_var(missing_treated_df)

X,Y= splitdata(drop_const_df)

std_scalar=StandardScaler()
arr1=std_scalar.fit_transform(X)
xtrain,xtest,ytrain,ytest=train_test_split(arr1,Y)

lr=LinearRegression()
lr.fit(xtrain,ytrain)


pickle.dump(lr,open("Admission_lr_model.sav",'wb'))
pickle.dump(std_scalar,open("std_scalar.sav",'wb'))