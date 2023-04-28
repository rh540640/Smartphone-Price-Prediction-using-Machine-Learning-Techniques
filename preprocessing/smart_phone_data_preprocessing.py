# -*- coding: utf-8 -*-
"""Smart_Phone_Data_Preprocessing.ipynb
# SMART PHONE PRICE PREDICTION: Data Preprocessing
"""

df = pd.read_csv(r"SP_Preprocessed.csv")
df.drop(columns=df.columns[0], axis=1, inplace=True)
df.drop_duplicates(subset ="Model",
                     keep = "first", inplace = True)
df.set_index('Model', inplace=True)

"""## Data Structure"""

df.shape

df.head()

df.info()

"""## Data Pre-processing

### Basic Cleaning
"""

df.columns

"""#### Possible New Columns

Resolution Type

Battery Type

Quadcore Processor

Number of rear camera

Number of front camera

Storage Expanable or not

Operating System

Network Type

Maybe Clockspeed

Price Range

Single Sim

**Impossible**

Release Date

Weight

Clock Speed

4G

3G
"""

#renaming
df.rename(columns = {'Stars':'Ratings', 'Num_of_Ratings':'Number Of Ratings', 'Expandable':'Expandable Storage', 'Ram':'RAM'}, inplace = True)
#new columns
df[['Rear Camera','Front Camera']] = df.Camera.str.split("|",expand=True)
#Replacing Values
df['Number Of Ratings'] = df['Number Of Ratings'].str.replace(',','')
df['Number Of Ratings'] = df['Number Of Ratings'].str.replace('Ratings','')
df['Reviews'] = df['Reviews'].str.replace(',','')
df['Reviews'] = df['Reviews'].str.replace('Reviews','')
df['RAM'] = df['RAM'].str.replace('512 MB RAM','0.512')
df['RAM'] = df['RAM'].str.replace('512 MB RAM','0.512')
df['RAM'] = df['RAM'].str.replace('256 MB RAM','0.256')
df['RAM'] = df['RAM'].str.replace('768 MB RAM','0.768')
df['RAM'] = df['RAM'].str.replace('768 MB RAM','0.768')

df = pd.read_csv('SP_Preprocessed.csv')
df['RAM'] = df['RAM'].replace('GB RAM','')
df['RAM'] = df['RAM'].replace('100 MB ROM ','')
df['RAM'] = df['RAM'].replace('xpandable Upto 32 G','')
df['RAM'] = df['RAM'].replace('Expandable Upto 16 G','')
df['RAM'] = df['RAM'].replace(' RAM ','')
df['RAM'] = df['RAM'].replace('134 MB ROM ','')
df['RAM'] = df['RAM'].replace('160 MB ROM ','')
df['RAM'] = df['RAM'].replace('140 MB ROM ','')
df['RAM'] = df['RAM'].replace('3 GB ROM ','')
df['RAM'] = df['RAM'].replace('3 GB ROM ','')
df['RAM'] = df['RAM'].replace('16 GB RO','')
df['RAM'] = df['RAM'].replace('8 GB RO','')
df['RAM'] = df['RAM'].str.replace('32 GB RO','')
df['RAM'] = df['RAM'].str.replace('512 GB RO','')
df['RAM'] = df['RAM'].str.replace('8 GB RO','')
df['RAM'] = df['RAM'].str.replace('256 GB RO','')
df['RAM'] = df['RAM'].str.replace('64 GB RO','')
df['RAM'] = df['RAM'].str.replace('128 GB RO','')
df['RAM'] = df['RAM'].str.replace('E','')
df['RAM'] = df['RAM'].str.replace('MB','')
df['RAM'] = df['RAM'].str.replace('1 TB RO','')

df['Storage'] = df['Storage'].str.replace('GB ROM','')
df['Storage'] = df['Storage'].str.replace('MB RO','')
df['Storage'] = df['Storage'].str.replace('Expandable','')
df['Storage'] = df['Storage'].str.replace('Expandabl','')
df['Storage'] = df['Storage'].str.replace('GB R','')
df['Storage'] = df['Storage'].str.replace('TB ROM','')
df['Storage'] = df['Storage'].str.replace('M','')
df['Storage'] = df['Storage'].str.replace('O','')
df['Storage'] = df['Storage'].str.replace('GB','')

df['Expandable Storage'] = df['Expandable Storage'].str.replace('Expandable Upto','')
df['Expandable Storage'] = df['Expandable Storage'].str.replace('xpandable Upto','')
df['Expandable Storage'] = df['Expandable Storage'].str.replace('GB','')
df['Expandable Storage'] = df['Expandable Storage'].str.replace('to','')

df['RAM'].value_counts()

df['RAM'] = df['RAM'].str.replace('..512','.512')

df['RAM'] = pd.to_numeric(df['RAM'])

df[['Display Size','Display Type']] = df.Display.str.split(")",expand=True)

df['Display Size'] = df['Display Size'].str.replace( 'inch','')

df.rename(columns = {'Display Size':'Display_Size'}, inplace = True)

df[['Display_Size','Useless']] = df.Display_Size.str.split("(",expand=True)

df.drop(['Useless'], axis=1, inplace=True)

df[['Battery_(mAh)','Battery_Type']] = df.Battery.str.split("mAh",expand=True)

df.drop(['Battery'], axis=1, inplace=True)

df['Battery_(mAh)'] = df['Battery_(mAh)'].str.replace('ARM Cortex-A7 Processor','')
df['Battery_(mAh)'] = df['Battery_(mAh)'].str.replace('A13 Bionic Chip Processor','')
df['Battery_(mAh)'] = df['Battery_(mAh)'].str.replace('1 Year Manufacturer Warranty','')

df['Battery_Type'] = df['Battery_Type'].replace({' Li-Ion Battery': 'Lithium-Ion', ' Li-ion Battery': 'Lithium-Ion', ' Lithium-ion Battery': 'Lithium-Ion',
                                                 ' Lithium ion Battery': 'Lithium-Ion', ' Li-ion Battery Battery': 'Lithium-Ion', 
                                                 ' Lithium Ion Battery': 'Lithium-Ion'})

df['Battery_Type'] = df['Battery_Type'].replace({' Li-Polymer Battery': 'Lithium-Polymer', ' Polymer Battery': 'Lithium-Polymer', ' Li-polymer Battery': 'Lithium-Polymer',
                            ' Lithium Polymer Battery': 'Lithium-Polymer', ' Li Polymer Battery' : 'Lithium-Polymer', ' Lithium-polymer Battery' : 'Lithium-Polymer', 
                           ' Li-Poly Battery' : 'Lithium-Polymer', ' LiPo Battery' : 'Lithium-Polymer', ' Lithium-Ploymer Battery' : 'Lithium-Polymer',
                           ' Lithium polymer Battery' : 'Lithium-Polymer', ' Li-Polymer Battery Battery' : 'Lithium-Polymer',
                                                ' Li-Po Battery' : 'Lithium-Polymer'})

df['Battery_Type'] = df['Battery_Type'].replace({' Li-ion Polymer Battery': 'Li-ion Polymer', ' Lithium-ion Polymer Battery': 'Li-ion Polymer', ' Li-Ion Polymer Battery': 'Li-ion Polymer',
                            ' Lithium Polymer Battery': 'Li-ion Polymer', '' : 'Li-ion Polymer', ' Lithium Ion Polymer Battery' : 'Li-ion Polymer', 
                           ' Lithium-Ion Polymer Battery' : 'Li-ion Polymer', ' LiPo Battery' : 'Lithium-Polymer', ' Lithium-Ploymer Battery' : 'Lithium-Polymer',
                           ' Li-ion Polymer Battery Battery' : 'Lithium-Polymer',})

df.drop(['Unnamed: 16'], axis=1, inplace=True)

df[['Rear Camera1',
       'Rear Camera2', 'Rear Camera3', 'Rear Camera4', 'Rear Camera5']] = df[['Rear Camera1',
       'Rear Camera2', 'Rear Camera3', 'Rear Camera4', 'Rear Camera5']].fillna(value=0)

df['Rear Camera1'] = df['Rear Camera1'].str.replace(' Primary Camera ','')

df['Rear Camera5'] = df['Rear Camera5'].str.replace("MP ", "")

df['Rear Camera5'].unique()

df['Front Camera1'] = df['Front Camera1'].fillna(df['Front Camera1'].value_counts().index[0])

df['Front Camera1'] = df['Front Camera1'].str.replace('MP','')

df['Front Camera2'] = df['Front Camera2'].str.replace('MP Dual Front Camera','')

df['Front Camera2'] = df['Front Camera2'].fillna(0)

df['Rear Camera4'] = df['Rear Camera4'].fillna(0)

df['Display Type'].value_counts()

df['FWVGA+ Display'].value_counts()

df['Display Type'].unique()

df.loc[df["Display Type"] == " Quad HD Display", "Quad HD Display"] = 1

#df.loc[df['Display Type'].str.contains(' HVGA Display'), 'HVGA Display'] = 1

df[['FWVGA Display', 'WVGA Display', 'HVGA Display', 'Normal Display',
       'HD Display', 'Full HD Display', 'quarter HD Display',
       'HD+ Display', 'NA Display', 'FWVGA+ Display',
       'Full HD+ Display', 'QVGA Display', 'Quad HD+ Display',
       'Quad HD Display', 'Full HD+ AMOLED Display',
       'Full HD+ Super AMOLED Display', 'Retina Display',
       'Retina HD Display', 'Super Retina XDR Display',
       'Full HD+ E3 Super AMOLED Display', 'Liquid Retina HD Display']] = df[['FWVGA Display', 'WVGA Display', 'HVGA Display', 'Normal Display',
       'HD Display', 'Full HD Display', 'quarter HD Display',
       'HD+ Display', 'NA Display', 'FWVGA+ Display',
       'Full HD+ Display', 'QVGA Display', 'Quad HD+ Display',
       'Quad HD Display', 'Full HD+ AMOLED Display',
       'Full HD+ Super AMOLED Display', 'Retina Display',
       'Retina HD Display', 'Super Retina XDR Display',
       'Full HD+ E3 Super AMOLED Display', 'Liquid Retina HD Display']].fillna(value=0)

df['Model'].str.contains("5G").value_counts()

df.loc[df['Model'].str.contains('5G'), '5G'] = 1

df['5G'].value_counts()

df[['5G']] = df[['5G']].fillna(value=0)

df[['Number of Sim Slots']] = df[['Number of Sim Slots']].fillna(value=2)

df["Operating System"].fillna("Android", inplace = True)

df['Operating System'].unique()

df.loc[df["Operating System"] == "Android", "Android"] = 1
df.loc[df["Operating System"] == "Windows", "Windows"] = 1
df.loc[df["Operating System"] == "iOS", "iOS"] = 1

df[["Android", "Windows", "iOS"]] = df[["Android", "Windows", "iOS"]].fillna(value=0)

df = pd.read_csv(r"C:\PROJECT\SP_Preprocessed.csv")

df = df.drop_duplicates(subset=['Model'])

df.set_index('Model', inplace=True)

convert_dict = {'Android': int,
                'Windows': int,
               'iOS': int}  
  
df = df.astype(convert_dict)  
print(df.dtypes)

"""## RUN HERE"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import warnings
warnings.filterwarnings('ignore')

#run here
df = pd.read_csv('SP_Preprocessed.csv')
df.set_index('Model', inplace=True)
df.head()

df.shape

df.isnull().sum()

"""-------------------------------------"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv(r"SP_Preprocessed.csv")
df.set_index('Model', inplace=True)

df.shape

df.head()

df.columns

df.info()

df.drop(['Processor', 'Display Type', 'Battery_Type', 'Brands', 'Operating System'], axis=1, inplace=True)

df['RAM'] = df['RAM'].fillna(df['RAM'].value_counts().index[0])
df['Storage'] = df['Storage'].fillna(df['Storage'].value_counts().index[0])
df['Battery_(mAh)'] = df['Battery_(mAh)'].fillna(df['Battery_(mAh)'].value_counts().index[0])
df['Warranty'] = df['Warranty'].fillna(df['Warranty'].value_counts().index[0])

df.isnull().sum()

df['iOS'].unique()



df.to_csv(r"C:\Users\richa\Desktop\SP_Preprocessed.csv")

#def price_range(value):
#    if value < 10000:
#        return 0
#    if 10000 <= value < 20000:
#        return 1
#    elif 20000 <= value < 30000:
#        return 2
#    elif value >= 30000:
#        return 3
#df['Price Range'] = df['Price'].map(price_range)
#       df.drop(['Price'], axis=1, inplace=True)

"""---------------------------"""