import pandas as pd
from sklearn.model_selection import train_test_split

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
    return X,Y


def train_test_splitfun(arr1,Y):
    xtrain,xtest,ytrain,ytest=train_test_split(arr1,Y,test_size=.2,random_state=0)
    return xtrain,xtest,ytrain,ytest