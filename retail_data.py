import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
data = pd.read_csv('data.csv', encoding = 'latin-1')
data.shape
data.columns
data.info()
data.head(5)
#checking for null value
data.isna().sum()
data = data.drop(['CustomerID'], axis = 1)#axis = 1 means columns wise
data.columns
data.dtypes
data['Description'].head(5)
data['Description'].value_counts().head(5)
#encode Description
data['Description'] = data['Description'].map({'WHITE HANGING HEART T-LIGHT HOLDER': 1, 'REGENCY CAKESTAND 3 TIER': 2,'JUMBO BAG RED RETROSPOT': 3,'JUMBO BAG RED RETROSPOT': 3,
    'PARTY BUNTING': 4, 'LUNCH BAG RED RETROSPOT': 5})
data['Description'].value_counts().head(5)
data.dtypes
data['InvoiceNo'].head(5)
data['InvoiceNo'].value_counts().head()
#again checking for null value
data.isna().sum()
mode = data['Description'].mode()[0]
mode
data.info()
#droped InvoiceDate
drop_data = data.drop(['InvoiceDate'], axis = 1)
df_country = pd.read_csv('country_codes.csv')
df_country.head(4)
#merging the dataset
df_final = pd.merge(data, df_country, on= 'Country', how = 'left')
df_final.head(5)
#filling the missing values in discription with mode
df_final['Description'] = df_final['Description'].fillna(mode, inplace = True)
#checking null value
df_final.isna().sum()
df_final.Description.value_counts()
#checing the column
df_final.columns
df_final.isna().sum()#Description = 541909
df_final.shape
df_final.Description
data['Description']
df_final.Description
