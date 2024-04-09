import pandas as pd

#Extract data
def Readdata():
    df=pd.read_csv('data/Admission_Prediction.csv')
    return df

#Handling missing treatment
def missing_treatment(df):
    df['GRE Score'].fillna(df['GRE Score'].mean(),inplace=True)
    df['TOEFL Score'].fillna(df['TOEFL Score'].mean(),inplace=True)
    df['University Rating'].fillna(df['University Rating'].mean(),inplace=True)
    return df


#Drop constant variable
def drop_const_var(df):
    df.drop(columns=['Serial No.'],axis=1,inplace=True)
    return df


def splitdata(df):
    X=df.drop(columns=['Chance of Admit'],axis=1)
    Y=df['Chance of Admit']

#pyscrips
std_scalar=StandardScaler()
arr1=std_scalar.fit_transform(X)
df1=pd.DataFrame(arr1,columns=X.columns)

lr=LinearRegression()
lr.fit(xtrain,ytrain)

import pickle
pickle.dump(lr,open("Admission_lr_model.sav",'wb'))

def train_test_split(arr1,Y):
    xtrain,xtest,ytrain,ytest=train_test_split(arr1,Y,test_size=.2,random_state=0)
    return xtrain,xtest,ytrain,ytest