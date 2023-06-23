
import ml
import pandas as pd

def predict(x):
    li=[]
    k=ml.fmc_model()

    df = pd.read_excel('OPENING AND CLOSING FIRST ROUND 2021.xlsx', index_col=False, skiprows=3)
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header
    cat = df["ALLOTTED CATEGORY"].unique()
    df = df.drop("DOMICILE", axis=1)
    df = df.drop("NATIONAL PLAYER", axis=1)

    o,c=x,x
    arr=[]

    start=500
    end=500
    index,count=0,0


    while(True):
        if count==5:
            break
        if(index%2==0):
            o=o-500
            r=k.predict([[o,c]])
            if r not in arr:
                arr.append(r)
                col=df["INSTITUTE NAME"][df["S.NO"]==r[0]]
                bran=df["BRANCH"][df["S.NO"]==r[0]]
                count+=1
                index+=1
            else:
                index+=1
        else:
            c=c+500
            r=k.predict([[o,c]])
            if r not in arr:
                arr.append(r)
                col=df["INSTITUTE NAME"][df["S.NO"]==r[0]]
                bran=df["BRANCH"][df["S.NO"]==r[0]]
                count+=1
                index+=1
            else:
                index+=1
    for i in arr:
        li.append(df[df["S.NO"]==i[0]])
    return li

if __name__=="__main__":
    
    k=predict(17000)
    print(len(k))
    print(k)


