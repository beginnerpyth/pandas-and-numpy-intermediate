import pandas as pd
import numpy as np
bios=pd.read_csv('bios.csv')
results=pd.read_csv('results.csv')
pand=pd.read_csv('pand.csv')
nocs=pd.read_csv('noc_regions.csv')
#print(bios.head())
#print(pand.columns)
#print(pand.info)
#print(pand.dtypes)
#print(pand.describe)
#print(pand.tail())
#print(pand.iloc[0:3,1:3])
#print(pand.loc[0:4,'Calories'])
#pand.index=pand.Calories
#print(pand.head())
#print(pand.sample())
#print(bios.loc[bios['height_cm']>165][['name','born_country']])
#print(bios[bios['height_cm']>170][['name','born_country']])
#print(bios[(bios['height_cm']>180)&(bios['born_country']=='USA')])
#print(bios[bios['name'].str.contains('Keith')&(bios['born_country'].isin(['USA']))])#isin use garda jaile panio([])
#print(bios[bios['born_country'].isin(['USA'])&(bios['name'].str.startswith('Keith'))])
#print(bios[bios['born_country'].isin(['USA'])&(bios['name'].str.startswith('Keith'))][['height_cm','name']])
#print(bios.query('born_country=="USA" and born_city=="Washington"'))
print(pand.columns)
#pand['Maxpulse']=130
#pand.rename(columns={'Duration':"Dur"},inplace=True)
#print(pand.columns)
#adding and removing columns

#pand['Newpulse']=np.where(pand['Pulse']<110,112,132)
#pand['Newpulse']=1.33

#print(pand.drop(index=0,inplace=True))
#print(pand.drop(columns="Newpulse",inplace=True))#we cn specofoy which columns or row by index and columns

#pand['Total intake']=pand['Pulse']*pand['Maxpulse']*pand['Calories']
#bios['first_name']=bios['name'].str.split(' ').str[0]#after splitting i want the first index
#print(bios['first_name'])
#bios['height_cat']=bios['height_cm'].apply(lambda x:'short' if x<160 else('average' if x<170 else "Tall"))
#print(bios[['name','height_cat']])
#using function lets add columns
#def add(yes):
#    if yes["height_cm"]<160 and yes["weight_kg"]<70:
#        return "light weight"
#    elif yes["height_cm"]<170 and yes['weight_kg']<80:
#        return"middleweight"
#    else:
#        return "heavyweight"
#bios["weight_cat"]=bios.apply(add,axis=1)
#print(bios['weight_cat'])
#merging and concatenating data
print(nocs.columns)
#new_csv=pd.merge(bios,nocs,left_on="born_country",right_on="NOC",how="left")#it means left columns untouched and right columns arrange ifit sames or becomes nan it different

#print(new_csv.columns)
#print(new_csv[['born_country','NOC_x',"NOC_y","region","notes"]])
another=pd.merge(bios,results,on='athlete_id',how='left')
print(another.columns)

# print(another[['noc','team','year']])
#concat
#usa=bios[bios['born_country']=='USA']#we use bios[bios[]] to extracty value not only boolean
#gbr=bios[bios['born_country']=='GBR']
#c=pd.concat([usa,gbr])#we use[]to make one argument
#print(c.head())
#handling null valuws
pand.loc[1:2,"Pulse"]=np.nan
print(pand.head())
#print(pand.isna().sum())#it shows where is nan value
#print(pand.isna())#just gives boolen value back
#print(pand.fillna(99))#it changes nan to specofoc value

#print(pand.fillna(pand['Pulse'].mean()))#it makes nan to be mean value
#print(pand.fillna(pand['Pulse'].interpolate(),inplace=True))#to makes interpolate we need sorrounding value to be non nan
#print(pand.head())
#pand['Pulse']=pand['Pulse'].interpolate()#its used to make the nan value a interpolate 
#print(pand.head())
#to drop the null value there are ways
#print(pand.dropna())#it drops the whole row and needs()
#print(pand.dropna(subset=['Pulse'],inplace=True))#now it removes the one pulse has null value and inplace changes modifes
#print(pand.head())
#we can even msasking
#print(pand.isna())
#print(pand.isna().sum())
#print(pand[pand['Pulse'].isna()])#it extrats the data in pulse which has na
#print(pand[pand['Pulse'].notna()])#it extratcs the data in pulse which has not na
#aggregrating data
#print(bios['born_city'].value_counts())#it gives the data whcih has hightes number of people born from
#print(bios[bios['born_country']=='USA']['born_region'].value_counts())#condition plus values count
#print(pand.groupby(['Pulse'])['Maxpulse'].sum())#it sums the value of maxpulse which pulse has same value
#print(pand.groupby(['Pulse']).agg({'Maxpulse':"sum","Calories":'mean'}))#when doing rename and agg func we use{}
#pivot=pand.pivot(index='Pulse',columns='Maxpulse',values='Caloies')
#print(pivot)
bios['born']=pd.to_datetime(bios['born_date'])
bios['year']=bios['born'].dt.year
#print(bios['year'].value_counts())#counts the highest value 
#print(bios.groupby(['year'])['name'].count().reset_index().sort_values('name',ascending=False))  
print(pand[pand['Calories']>100])    