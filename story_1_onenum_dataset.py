# -*- coding: utf-8 -*-
"""Story_1-onenum-dataset

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B9SqIAuLaQdJWfrNCpEkpLq1DQ0skDbS

AIRBNB PRICES ON THE FRENCH RIVIERA
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/1_OneNum.csv")
df['price'].describe()

df['price']=df['price'][(df['price']<300)]
df['price'].describe()

# check out missing data
total = df.isnull().sum().sort_values(ascending=False)
percent = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
missing_df = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing_df.head(20)

# Select only numeric data and impute missing values as 0
numerics = ['uint8','int16', 'int32', 'int64', 'float16', 'float32', 'float64']
data = df \
    .select_dtypes(include=numerics) \
    .fillna(0) \
    .values

a=df["price"]<300
a.head()

"""Histogram"""

d=sns.displot(df["price"],fill="#69b3a2", color="#e9ecef", alpha=0.9)
d.set(title='Night price distribution of Airbnb appartements')
plt.show()
## bin size =10
d1=sns.displot(df["price"],bins=10,fill="#69b3a2", color="#e9ecef", alpha=0.9)
d1.set(title='Night price distribution of Airbnb appartements')
plt.show()
## bin size =2
d2=sns.displot(df["price"],bins=2,fill="#69b3a2", color="#e9ecef", alpha=0.9)
d2.set(title='Night price distribution of Airbnb appartements')
plt.show()

"""Density Plot"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming your data is in a pandas DataFrame named 'data'
data_filtered = df[df['price'] < 300]

# Create the plot
sns.set_style("whitegrid")
sns.kdeplot(data=data_filtered, x="price", bw_adjust=10, fill=True, alpha=0.7, color="#69b3a2")
plt.title("Bandwidth: 10")
plt.show()



sns.kdeplot(data=data_filtered, x="price", bw_adjust=2, fill=True, alpha=0.7, color="#69b3a2")
plt.title("Bandwidth: 2")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming your data is in a pandas DataFrame named 'data'
data_filtered = df[df['price'] < 300]

# Create the plot
sns.set_style("whitegrid")
sns.kdeplot(data=data_filtered, x="price", bw_adjust=2, fill=True, alpha=0.7, color="#69b3a2")
plt.title("Bandwidth: 2")
plt.show()

