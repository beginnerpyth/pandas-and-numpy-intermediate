import pandas as pd
import numpy as np
bios=pd.read_csv('bios.csv')
nocs=pd.read_csv('noc_regions.csv')
pand=pd.read_csv('pand.csv')
#aggregrating the function
bios['born_date']=pd.to_datetime(bios['born_date']) 
bios['year']=bios['born_date'].dt.year
bios['month']=bios['born_date'].dt.month
print(bios.columns)
#print(pand['Pulse'].interpolate())
#print(pand.groupby(['Maxpulse'])['Calories'].sum())#aggregrate the value opf each maxpulse summing the calories total
#print(pand.groupby(['Maxpulse'])['Calories'].mean())
#print(pand.groupby(['Pulse','Maxpulse']).agg({'Calories':'sum','Duration':'mean'}))
#print(bios[bios['born_country']=='USA']['born_region'].value_counts())
#print(bios[bios['born_country']=='USA']['born_region'].value_counts())
#pivot=pand.pivot(columns='Maxpulse',index='Pulse',values='Calories',aggfun='mean')
#print(pivot)
print(bios.groupby(['year','month'])['name'].count().reset_index().sort_values('name',ascending=False))