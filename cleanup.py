import pandas as pd

babolat = pd.read_csv('Babolat.csv')
wilson = pd.read_csv('Wilson.csv')
head = pd.read_csv('Head.csv')
yonex = pd.read_csv('Yonex.csv')

babolat.name = 'babolat'
wilson.name = 'wilson'
head.name = 'head'
yonex.name = 'yonex'
     
# position starts from 0 not 1            
def choose_unit(df,col_name,position):
    for i in range(0,len(df[col_name])):
        if type(df.loc[i,col_name])==str:
            if '/' in df.loc[i,col_name]:
                df.loc[i,col_name] = df.loc[i,col_name].split('/')[position]
    return df            
            
def exclude_junior(df):
    df = df[~df.Racket_Name.str.contains('Junior')]
    return df
   
cols_drop = ['String_Tension','String_Pattern','Color','Grip_Type',
 'Composition','Strung_Weight']
 
racket_brands = [babolat,wilson,head,yonex]
 
for brand in racket_brands:
    file_name = brand.name
    brand = choose_unit(brand,"Head_Size",0)
    brand = choose_unit(brand,"Length",0)
    brand = choose_unit(brand,"Balance",2)
    brand = brand.drop(cols_drop,axis=1)
    brand = exclude_junior(brand)
    brand.to_csv('./cleaned_output/'+file_name+'.csv',index=False)
    
# Question..
# If put file_name just before to_csv, it wouldn't work
# If drop and exclude_junior first, also doesn't work
    