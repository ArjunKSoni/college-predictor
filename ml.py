import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
def fmc_model():


    le=LabelEncoder()
    rfc=RandomForestClassifier(n_estimators= 20, criterion="entropy")
    df=pd.read_excel('OPENING AND CLOSING FIRST ROUND 2021.xlsx',index_col=False, skiprows=3)
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header
    df['INSTITUTE NAME']=LabelEncoder().fit_transform(df['INSTITUTE NAME'])
    df['INSTITUTE TYPE']=LabelEncoder().fit_transform(df['INSTITUTE TYPE'])
    df['INSTITUTE FW']=LabelEncoder().fit_transform(df['INSTITUTE NAME'])
    df['BRANCH']=LabelEncoder().fit_transform(df['BRANCH'])
    df['ALLOTTED CATEGORY']=LabelEncoder().fit_transform(df['ALLOTTED CATEGORY'])
    df=df.drop("DOMICILE",axis=1)
    df=df.drop("NATIONAL PLAYER",axis=1)
    df['FW']=LabelEncoder().fit_transform(df['FW'])
    x=df[["JEE OPENING RANK","JEE CLOSING RANK"]]
    y=df["S.NO"]
    y=y.astype('int')

    rfc.fit(x,y)
    return rfc


