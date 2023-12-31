# -*- coding: utf-8 -*-
"""flight price prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NVEztYR-Y6aPYXt7T4VgZ4i46vdyKLgg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('/content/Clean_Dataset.csv')
df1=pd.read_csv('/content/business.csv')

df.head()

df.tail()

df1.head()

df.info()

df.describe()

df.duplicated().sum()

df.dtypes

df.nunique()

df.isnull().sum()

df.eq(0).sum()

sns.heatmap(df.corr())

cr= df.corr()
cr_df= cr['price'].sort_values(ascending= False)
cr_df

# cols = df.columns
# for col in cols:
#   print(col)

#   print(df[col].unique())
#   print('------------------')

#1

df['airline'].value_counts()

sns.countplot(df, x='airline')
plt.title('Airline Count')
plt.show()

sns.countplot(df, x='source_city')
plt.title('Popular Source City')
plt.show()

sns.countplot(df, x='destination_city')
plt.title('Popular Destination City')
plt.show()

sns.countplot(df, x='stops')
plt.title('No. of stops')
plt.show()

sns.countplot(df, x='arrival_time')
plt.title('Popular arrival Time')
plt.xticks(rotation=90)
plt.show()

sns.countplot(df, x='departure_time')
plt.title('Popular departure Time')
plt.xticks(rotation=90)
plt.show()

#2

df.groupby('airline').sum().sort_values('price',ascending=False)[['price']]

#3

ec = df[df['class'] == 'Economy']
ec['airline'].value_counts()

ec.groupby('airline').sum().sort_values('price',ascending=False)[['price']]

sns.countplot(ec, x='airline')
plt.title('Popular Economy Airline')

plt.show()

sns.barplot(ec, x='airline', y='price')
plt.title('Popular Economy Airline Price')

plt.show()

bs = df[df['class'] == 'Business']
bs['airline'].value_counts()

bs.groupby('airline').sum().sort_values('price',ascending=False)[['price']]

sns.countplot(bs, x='airline')
plt.title('Popular Business Airline')

plt.show()

sns.barplot(bs, x='airline', y='price')
plt.title('Popular Business Airline Price')

plt.show()

df['stops'].unique()

df['stops'] = df['stops'].replace({'zero': 0, 'one':1, 'two_or_more': 2})

df=df.drop('Unnamed: 0', axis=1)

df.head()

df['class'].unique()

df['class'] = df['class'].replace({'Economy': 1, 'Business':2})

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder

df['airline'] = df['airline'].replace({'SpiceJet': 1, 'AirAsia':2, 'GO_FIRST':3, 'Indigo':4, 'Air_India':5, 'Vistara':6})

df['arrival_time'].unique()

label_encoder= LabelEncoder()

df['arrival_time'] = label_encoder.fit_transform(df['arrival_time'])
df['departure_time'] = label_encoder.fit_transform(df['departure_time'])

df.head()

sns.countplot(x=df['source_city'],hue=df['destination_city'])
plt.show()

# we can see that the airline travelling between Delhi to Mumbai has the most no. of counts among all the travel routes.

df['source_to_destination']= df['source_city']+ " to "+ df['destination_city']

df.head()

df['source_to_destination'].value_counts()

sns.barplot(df, x='source_to_destination', y= 'price')
plt.xticks(rotation=90)
plt.title('Price among diff airline routes')
plt.show()

"""chennai to bangalore has the highest price for the airline."""

sns.barplot(df, x='source_to_destination', y= 'duration')
plt.xticks(rotation=90)
plt.title('Duration of diff airline routes')
plt.show()

"""Kolkata to chennai has the highest duration."""

airline_used = df.groupby(['source_to_destination', 'airline']).size().sort_values(ascending = False)
airline_used

sns.countplot(data = df,x='source_city',hue = 'airline')
plt.show()

ec['source_city'].value_counts()

bs['source_city'].value_counts()

df.groupby('class').mean().sort_values('price',ascending=False)[['duration','price']]

df['days_left'].unique()

df.groupby('days_left').mean().sort_values('price',ascending=False)['price']

ec.groupby('days_left').mean().sort_values('price',ascending=False)['price']

bs.groupby('days_left').mean().sort_values('price',ascending=False)['price']

#hence we can clearly see the price variations with respect to the lesser days of depature leading to higher prices.

df.head()

df['source_city'] = label_encoder.fit_transform(df['source_city'])
df['destination_city'] = label_encoder.fit_transform(df['destination_city'])
df['source_to_destination'] = label_encoder.fit_transform(df['source_to_destination'])

df=df.drop('flight',axis=1)

df.head()

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from sklearn.metrics import explained_variance_score,mean_absolute_error,r2_score

X= df.drop(['price'], axis=1)
y = df.price

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 0)

from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsRegressor

# lr = LogisticRegression()
# lr.fit(X_train, y_train)

# y_pred= lr.predict(X_test)

# mse = mean_squared_error(y_test, y_pred1)
# r2_square = r2_score(y_test,y_pred1)
# rms = np.sqrt(mean_squared_error(y_test, y_pred1))
# print(f" R-squared: {r2_square}")
# print(f'Mean Squared Error: {mse}')
# print(f'Root Mean Squared Error: {rms}')

rf= RandomForestRegressor()
rf.fit(X_train, y_train)

y_pred2= rf.predict(X_test)

mse = mean_squared_error(y_test, y_pred2)
r2_square = r2_score(y_test,y_pred2)
rms = np.sqrt(mean_squared_error(y_test, y_pred2))
print(f" R-squared: {r2_square}")
print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rms}')

dt= DecisionTreeRegressor(max_depth=8)
dt.fit(X_train, y_train)

y_pred3= rf.predict(X_test)

mse = mean_squared_error(y_test, y_pred3)
r2_square = r2_score(y_test,y_pred3)
rms = np.sqrt(mean_squared_error(y_test, y_pred3))
print(f" R-squared: {r2_square}")
print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rms}')

from sklearn.ensemble import HistGradientBoostingRegressor, GradientBoostingRegressor, ExtraTreesRegressor
from sklearn.svm import SVR
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor

xgb=XGBRegressor()
xgb.fit(X_train, y_train)

y_pred4=xgb.predict(X_test)

mse = mean_squared_error(y_test, y_pred4)
r2_square = r2_score(y_test,y_pred4)
rms = np.sqrt(mean_squared_error(y_test, y_pred4))
print(f" R-squared: {r2_square}")
print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rms}')

lgb= LGBMRegressor()
lgb.fit(X_train, y_train)

y_pred5=lgb.predict(X_test)

mse = mean_squared_error(y_test, y_pred5)
r2_square = r2_score(y_test,y_pred5)
rms = np.sqrt(mean_squared_error(y_test, y_pred5))
print(f" R-squared: {r2_square}")
print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rms}')

gb= GradientBoostingRegressor()
gb.fit(X_train,y_train)

y_pred6=gb.predict(X_test)

mse = mean_squared_error(y_test, y_pred6)
r2_square = r2_score(y_test,y_pred6)
rms = np.sqrt(mean_squared_error(y_test, y_pred6))
print(f" R-squared: {r2_square}")
print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rms}')

hgb= HistGradientBoostingRegressor()
hgb.fit(X_train,y_train)

y_pred7=hgb.predict(X_test)

mse = mean_squared_error(y_test, y_pred7)
r2_square = r2_score(y_test,y_pred7)
rms = np.sqrt(mean_squared_error(y_test, y_pred7))
print(f" R-squared: {r2_square}")
print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rms}')

