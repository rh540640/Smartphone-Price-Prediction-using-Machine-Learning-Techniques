# -*- coding: utf-8 -*-
"""TEST CODE.ipynb


# SMART PHONE PRICE PREDICTION

> Richard H

#### Import Libraries
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import re
import warnings
import seaborn as sns
warnings.filterwarnings('ignore')

"""## Data Structure"""

from google.colab import files
uploaded = files.upload()
import io
df = pd.read_csv(io.BytesIO(uploaded['SP_Preprocessed.csv']))
df.set_index('Model', inplace=True)

df.shape

df.head()

df.info()

df.isnull().sum()

df.describe().T

"""## Data Preprocessing"""

df1 = df.drop(['Operating System', 'Brands', 'Processor', 'Display Type', 'Battery_Type'], axis=1)
#df1 = df.drop(['Operating System', 'Brands', 'Processor', 'Display Type', 'Battery_Type', 'Colour'], axis=1)

#df3 = df1.sort_values(by="Price", ascending=True)

#df_split = np.array_split(df3, 4)

df['Processor'] = df['Processor'].fillna(df['Processor'].value_counts().index[0])
df['Battery_Type'] = df['Battery_Type'].fillna(df['Battery_Type'].value_counts().index[0])

def price_range(value):
    if value < 5900:
        return 0
    if 5900 <= value <= 8499:
        return 1
    elif 8499 < value < 12949:
        return 2
    elif value >= 12949:
        return 3
df1['Price Range'] = df1['Price'].map(price_range)

plt.figure(figsize=(10,6))
sns.countplot(data=df1,x='Price Range')

"""## EDA"""

def OS(x):
    return df[df['Operating System'] == x][['Price', 'Number of Sim Slots', 'Ratings',
       'Number Of Ratings', 'RAM', 'Storage', 'Expandable Storage', 'Front Camera1', 'Rear Camera1', 'Display Type', 'Battery_(mAh)']]

OS('Windows')

def OS(x):
    return df[df['Operating System'] == x][['Price', 'Number of Sim Slots', 'Ratings',
       'Number Of Ratings', 'RAM', 'Storage', 'Expandable Storage', 'Front Camera1', 'Rear Camera1', 'Display Type', 'Battery_(mAh)']]

OS('iOS')

def FiveG(x):
    return df[df['5G'] == x][['Price', 'Number of Sim Slots', 'Ratings',
       'Number Of Ratings', 'RAM', 'Storage', 'Expandable Storage', 'Front Camera1', 'Rear Camera1', 'Display Type', 'Battery_(mAh)']]

FiveG(1).head()

df.columns

Range = df1['Price Range'].value_counts().to_frame()
Range.to_csv('Range.csv')

Ratings = df1['Ratings'].value_counts().to_frame()
Ratings.to_csv('Ratings.csv')

type = df['Display Type'].value_counts().to_frame()
type.to_csv('type.csv')

"""Correlation with Price"""

correlated_features = set()
correlation_matrix = df1.corr()
corr_cols_order = df1.corr()['Price'].sort_values(ascending=False).index
corr_cols_order

"""## Data Visualisation"""

import seaborn as sns
plt.subplots(figsize = (18, 18))
sns.heatmap(df1.corr())
plt.savefig('Heatmap.png')

from PIL import Image
from wordcloud import STOPWORDS
mask = np.array(Image.open('mobile.png'))
nationality = " ".join(n for n in df['Brands'])
from wordcloud import WordCloud
plt.figure(figsize=(12,9))
wc = WordCloud(stopwords=STOPWORDS,
               mask=mask, background_color="white",
               max_words=2000, max_font_size=256,
               random_state=42, width=mask.shape[1],
               height=mask.shape[0]).generate(nationality)
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
plt.savefig('Wordmap.png')

"""### Bar Chart"""

plt.figure(figsize = (15,7))
df['Brands'].value_counts().head(50).plot.bar(color = 'orangered', grid=False)
plt.title('Number of smartphones of different brands')
plt.xlabel('Brand')
plt.ylabel('Count')
plt.show()
plt.savefig('Barchart-Brands.png')

plt.figure(figsize=(12, 10))
sns.countplot(x=df['Price'])
plt.xticks(rotation=90);
plt.savefig('PriceRange.png')

plt.figure(figsize=(12, 10))
sns.countplot(x=df['Ratings'])
plt.xticks(rotation=90);
plt.savefig('Ratingscount.png')

plt.figure(figsize=(12, 10))
sns.countplot(x=df['Display Type'])
plt.xticks(rotation=90);
plt.savefig('Displaysize.png')

"""### Histogram"""

df1.hist(bins=25,figsize=(20,20));

"""### Scatterplot"""

sns.set()
cols = ['Number of Sim Slots', 'Ratings', 'Number Of Ratings', 'Reviews', 'RAM',
       'Storage', 'Expandable Storage', 'Warranty','Price', 'Number of Front Cameras',
       'Display_Size', 'Battery_(mAh)', 'Number Of Rear Cameras', 'Rear Camera1', 'Rear Camera2',
       'Rear Camera3', 'Rear Camera4', 'Front Camera1', 'Front Camera2'] 
sns.pairplot(df1[cols], height = 2.5)
plt.show()

"""#### Strong Positive Correlation

Number of Ratings and reviews, Display Size and Battery (mAh), RAM and Rear Camera1, Price and RAM, Rear Camera1 and Display Size, Front Camera1 and Display Size
"""

sns.set(rc={'figure.figsize':(20,8)})
sns.scatterplot(data=df, x='Reviews', y='Number Of Ratings', hue='Ratings').set(title='Number of Rating vs Reviews')

sns.set(rc={'figure.figsize':(20,8)})
sns.scatterplot(data=df, x='Display_Size', y='Battery_(mAh)').set(title='Display Size vs Battery')

sns.set(rc={'figure.figsize':(20,8)})
sns.scatterplot(data=df, x='RAM', y='Rear Camera1').set(title='RAM vs Rear Camera')

sns.set(rc={'figure.figsize':(20,8)})
sns.scatterplot(data=df, x='RAM', y='Price').set(title='RAM vs Rear Camera')

sns.set(rc={'figure.figsize':(20,8)})
sns.scatterplot(data=df, x='Rear Camera1', y='Display_Size').set(title='Rear Camera vs Display Size')

sns.set(rc={'figure.figsize':(20,8)})
sns.scatterplot(data=df, x='Front Camera1', y='Display_Size').set(title='Front Camera vs Display Size')

sns.set_style("whitegrid", {'axes.grid' : False})
sns.relplot(data=df1, x="Number Of Ratings", y="Reviews",col="iOS", kind='line')

sns.displot(data=df1, x="Display_Size")

sns.displot(data=df, x="Storage", kde=True)

sns.set(rc={'figure.figsize':(20,8)})
sns.displot(data=df, x="Battery_(mAh)", hue="5G", multiple="stack")

sns.histplot(data=df, x="Price", kde=True)

sns.set(rc={'figure.figsize':(10,10)})
sns.histplot(data=df1, x="Battery_(mAh)", hue="Price Range", multiple="dodge", shrink=.8)

sns.kdeplot(data=df1, x="5G", hue="Price Range", multiple="stack")

sns.kdeplot(data=df, x="Price", hue="Operating System", multiple="fill")
plt.savefig('KDE Plot.png')

"""## Feature Scaling (Optionals)

### Standard Scaler
"""

df1.columns

from sklearn import preprocessing
scaler = preprocessing.StandardScaler().fit(df1)
df_scaled = scaler.transform(df1)
df_scaled = pd.DataFrame(df_scaled, columns = ['Number of Sim Slots', 'Ratings', 'Number Of Ratings', 'Reviews', 'RAM',
       'Storage', 'Expandable Storage', 'Expandable or Not', 'Warranty',
       'Price', 'Front Camera1', 'Front Camera2', 'Number of Front Cameras',
       'Display_Size', 'Battery_(mAh)', 'Rear Camera1', 'Rear Camera2',
       'Rear Camera3', 'Rear Camera4', 'Number Of Rear Cameras',
       'FWVGA Display', 'WVGA Display', 'HVGA Display', 'Normal Display',
       'HD Display', 'Full HD Display', 'quarter HD Display', 'HD+ Display',
       'NA Display', 'FWVGA+ Display', 'Full HD+ Display', 'QVGA Display',
       'Quad HD+ Display', 'Full HD+ AMOLED Display',
       'Full HD+ Super AMOLED Display', 'Retina Display', 'Retina HD Display',
       'Super Retina XDR Display', 'Full HD+ E3 Super AMOLED Display',
       'Liquid Retina HD Display', 'Quad HD Display', '5G', 'Android',
       'Windows', 'iOS', 'Price Range'])

df_scaled.shape

#df_scaled.drop(['Number Of Ratings', 'Reviews', 'Expandable Storage', 'Warranty'
#                , 'Android', 'Windows', 'Quad HD Display', 'Liquid Retina HD Display', 
#                'Rear Camera4', 'Rear Camera1'], axis = 1, inplace=True)

"""### Minmax Scaler"""

scaler = preprocessing.MinMaxScaler().fit(df)
df_scaled = scaler.transform(df)
df_scaled = pd.DataFrame(df_scaled, columns = ['Number of Sim Slots', 'Ratings', 'Number Of Ratings', 'Reviews', 'RAM',
       'Storage', 'Expandable Storage', 'Expandable or Not', 'Warranty',
       'Price', 'Front Camera1', 'Front Camera2', 'Number of Front Cameras',
       'Display_Size', 'Battery_(mAh)', 'Rear Camera1', 'Rear Camera2',
       'Rear Camera3', 'Rear Camera4', 'Rear Camera5',
       'Number Of Rear Cameras', 'FWVGA Display', 'WVGA Display',
       'HVGA Display', 'Normal Display', 'HD Display', 'Full HD Display',
       'quarter HD Display', 'HD+ Display', 'NA Display', 'FWVGA+ Display',
       'Full HD+ Display', 'QVGA Display', 'Quad HD+ Display',
       'Full HD+ AMOLED Display', 'Full HD+ Super AMOLED Display',
       'Retina Display', 'Retina HD Display', 'Super Retina XDR Display',
       'Full HD+ E3 Super AMOLED Display', 'Liquid Retina HD Display',
       'Quad HD Display', '5G', 'Price Range'])

"""### Normalization"""

scaler = preprocessing.Normalizer().fit(df)
df_scaled = scaler.transform(df)
df_scaled = pd.DataFrame(df_scaled, columns = ['Number of Sim Slots', 'Ratings', 'Number Of Ratings', 'Reviews', 'RAM',
       'Storage', 'Expandable Storage', 'Expandable or Not', 'Warranty',
       'Price', 'Front Camera1', 'Front Camera2', 'Number of Front Cameras',
       'Display_Size', 'Battery_(mAh)', 'Rear Camera1', 'Rear Camera2',
       'Rear Camera3', 'Rear Camera4', 'Rear Camera5',
       'Number Of Rear Cameras', 'FWVGA Display', 'WVGA Display',
       'HVGA Display', 'Normal Display', 'HD Display', 'Full HD Display',
       'quarter HD Display', 'HD+ Display', 'NA Display', 'FWVGA+ Display',
       'Full HD+ Display', 'QVGA Display', 'Quad HD+ Display',
       'Full HD+ AMOLED Display', 'Full HD+ Super AMOLED Display',
       'Retina Display', 'Retina HD Display', 'Super Retina XDR Display',
       'Full HD+ E3 Super AMOLED Display', 'Liquid Retina HD Display',
       'Quad HD Display', '5G'])

"""## Data Split"""

X = df1.drop(['Price', 'Price Range'],axis=1)
y = df1['Price']
#X = df_scaled.drop(['Price', 'Price Range'],axis=1)
#y = df_scaled['Price']
#y = df1['Price Range']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

"""## Dimensionality Reduction

### Feature Selection

#### ANOVA
"""

import sklearn.feature_selection
from sklearn.feature_selection import f_regression
from sklearn.feature_selection import SelectKBest
Values = f_regression(X, y, center=True)

Values

X_new = SelectKBest(f_regression, k=40).fit_transform(X, y)

"""## Modelling

## Regression

### Linear Regression

#### Hyperparameter Tuning
"""

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, GridSearchCV, StratifiedKFold
import warnings
warnings.filterwarnings('ignore')
reg = LinearRegression()
reg.get_params()
#fitintercept = [True, False]

copy_x = [True, False]
#postive = [True, False]
njobs = [-1]
param_grid = {
              'n_jobs': njobs}
grid = GridSearchCV(estimator=reg, 
                    param_grid=param_grid, 
                    cv = 10, 
                    scoring='r2')
grid.fit(X_train, y_train)

from sklearn.metrics import r2_score, mean_squared_error
print("Best Parameters", grid.best_params_)
pred = grid.predict(X_test)
r2 = r2_score(y_test, pred)
print('R2: ', r2)
err = np.sqrt(mean_squared_error(y_test, pred))
print('Root Mean Squared Error: ', err)

reg = LinearRegression()
reg.fit(X_train, y_train)
pred = reg.predict(X_test)

reg.coef_

reg.intercept_

y_test.shape

# multiple lines with legend
plt.figure(figsize=(23, 9))
plt.plot(np.arange(1,235),y_test,marker='.', color='b', label= 'Actual Value')
plt.plot(np.arange(1,235),pred, marker = '+', color = 'g',label = 'Predicted Value')
plt.xlabel("Index to Mobiles")
plt.ylabel("Actual and Predicted Value")
plt.title("Actual and Predicted Price Using Linear Regression ")
plt.legend();

"""### Random Forest Regressor"""

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, GridSearchCV, StratifiedKFold
import warnings
warnings.filterwarnings('ignore')
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

RFR = RandomForestRegressor()
RFR.get_params()

param_grid = {'bootstrap': [True], 
              'max_depth': [9],
              'max_features': ['auto'],              
              'n_estimators': [20]}
grid = GridSearchCV(estimator=RFR, 
                    param_grid=param_grid, 
                    cv = 9, 
                    scoring='r2')
grid.fit(X_train, y_train)
#param_grid = {'bootstrap': [True], 
#              'max_depth': [9],
#              'max_features': [1.0, 'auto', 'log2'],              
#              'n_estimators': [5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 20,100]}

print("Best Parameters", grid.best_params_)
pred = grid.predict(X_test)
r2 = r2_score(y_test, pred)
print('R2: ', r2)
err = np.sqrt(mean_squared_error(y_test, pred))
print('Root Mean Squared Error: ', err)

# multiple lines with legend
plt.figure(figsize=(14, 9))
plt.plot(np.arange(1,235),y_test,marker='.', color='b', label= 'Actual Value')
plt.plot(np.arange(1,235),pred, marker = '+', color = 'g',label = 'Predicted Value')
plt.xlabel("Index to Mobiles")
plt.ylabel("Actual and Predicted Value")
plt.title("Actual and Predicted Price using Random Forest Regressor")
plt.legend();
plt.savefig('Actual and predicted.png')

fig = plt.figure()
plt.figure(figsize=(20,20))
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(np.arange(1,235), y_test)
ax2.plot(np.arange(1,235), pred, 'g')
ax1.set_title("Actual Price")
ax2.set_title("Predicted Price")
plt.xlabel("Index to Mobiles")
plt.savefig('Subplots.png')

a, b = np.polyfit(y_test, pred, 1)

plt.figure(figsize=(14, 9))
plt.plot(y_test, pred,marker='.', color='g')
plt.plot(pred, a*pred+b, 'r') 
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual and Predicted Price")
plt.savefig('Predicted bs actual.png')

"""#### Metrics"""

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
print('MEA :',mean_absolute_error(y_test, pred))
print('R2  :',r2_score(y_test, pred))
print('MSE :',(mean_squared_error(y_test, pred)))
print('RMSE :',np.sqrt(mean_squared_error(y_test, pred)))
print('MAPE :',mean_absolute_percentage_error(y_test, pred))

"""#### Best Estimator"""

grid.best_estimator_.base_estimator_

grid.best_estimator_.estimators_

grid.best_estimator_.n_features_in_

grid.best_estimator_.feature_names_in_

grid.best_estimator_.n_outputs_

importance_gb = grid.best_estimator_.feature_importances_
importance_gb

X_train.columns

columns = X_train.columns
#Combine columns with feature importances
gbGraph = pd.Series(importance_gb, columns)
gbGraph

gbGraph.sort_values()

# Visualizing importance from our model

from matplotlib.pyplot import figure
figure(figsize = (10,10))
gbGraph.sort_values().plot.barh(color='b')
plt.title('Feature Importance')
plt.savefig('Feature Importance.png')

len(grid.best_estimator_.estimators_)

# first decision tree of the random forest
grid.best_estimator_.estimators_[0]

#We can plot a first Decision Tree from the Random Forest
from sklearn import tree
plt.figure(figsize=(20,20))
_ = tree.plot_tree(grid.best_estimator_.estimators_[0], feature_names=X_train.columns, filled=True, fontsize=7.5)
plt.savefig('First Decision Tree.png')

"""### Decision Tree Regressor"""

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import KFold, GridSearchCV, StratifiedKFold
import warnings
warnings.filterwarnings('ignore')
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
DTR = DecisionTreeRegressor()
DTR.get_params()

param_grid={"max_depth" : [1,3,5,7,9,11,12],
           "min_samples_leaf":[1,2,3,4,5,6,7,8,9,10],
           "max_features":[None],
           "max_leaf_nodes":[None,10,20,30,40,50,60,70,80,90] }
grid = GridSearchCV(estimator=DTR, 
                    param_grid=param_grid, 
                    cv = 10, 
                    scoring='r2')
grid.fit(X_train, y_train)

print("Best Parameters", grid.best_params_)
pred = grid.predict(X_test)
r2 = r2_score(y_test, pred)
print('R2: ', r2)
err = np.sqrt(mean_squared_error(y_test, pred))
print('Root Mean Squared Error: ', err)

# multiple lines with legend
plt.figure(figsize=(14, 9))
plt.plot(np.arange(1,235),y_test,marker='.', color='b', label= 'Actual Value')
plt.plot(np.arange(1,235),pred, marker = '+', color = 'g',label = 'Predicted Value')
plt.xlabel("Index to Mobiles")
plt.ylabel("Actual and Predicted Value")
plt.title("Actual and Predicted Price using Desicion Tree Regressor")
plt.legend();
plt.savefig('Actual and predicted.png')

fig = plt.figure()
plt.figure(figsize=(20,20))
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(np.arange(1,235), y_test)
ax2.plot(np.arange(1,235), pred, 'g')
ax1.set_title("Actual Price")
ax2.set_title("Predicted Price")
plt.xlabel("Index to Mobiles")
plt.savefig('Subplots.png')

a, b = np.polyfit(y_test, pred, 1)
plt.figure(figsize=(14, 9))
plt.plot(y_test, pred,marker='.', color='g')
plt.plot(pred, a*pred+b, 'r') 
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual and Predicted Price")
plt.savefig('Predicted bs actual.png')

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
print('MEA :',mean_absolute_error(y_test, pred))
print('R2  :',r2_score(y_test, pred))
print('MSE :',(mean_squared_error(y_test, pred)))
print('RMSE :',np.sqrt(mean_squared_error(y_test, pred)))
print('MAPE :',mean_absolute_percentage_error(y_test, pred))

grid.best_estimator_.base_estimator_

grid.best_estimator_.estimators_

grid.best_estimator_.n_features_in_

importance_gb = grid.best_estimator_.feature_importances_
importance_gb

X_train.columns

columns = X_train.columns
#Combine columns with feature importances
gbGraph = pd.Series(importance_gb, columns)
gbGraph

gbGraph.sort_values()

# Visualizing importance from our model

from matplotlib.pyplot import figure
figure(figsize = (10,10))
gbGraph.sort_values().plot.barh(color='b')
plt.title('Feature Importance of Desicion Tree Regressor')
plt.savefig('Feature Importance.png')

df1.columns

from IPython.display import display
import graphviz
from sklearn.tree import DecisionTreeClassifier, export_graphviz


display(graphviz.Source(export_graphviz(grid.best_estimator_, feature_names=['Number of Sim Slots', 'Ratings', 'Number Of Ratings', 'Reviews', 'RAM',
       'Storage', 'Expandable Storage', 'Expandable or Not', 'Warranty',
       'Front Camera1', 'Front Camera2', 'Number of Front Cameras',
       'Display_Size', 'Battery_(mAh)', 'Rear Camera1', 'Rear Camera2',
       'Rear Camera3', 'Rear Camera4', 'Number Of Rear Cameras',
       'FWVGA Display', 'WVGA Display', 'HVGA Display', 'Normal Display',
       'HD Display', 'Full HD Display', 'quarter HD Display', 'HD+ Display',
       'NA Display', 'FWVGA+ Display', 'Full HD+ Display', 'QVGA Display',
       'Quad HD+ Display', 'Full HD+ AMOLED Display',
       'Full HD+ Super AMOLED Display', 'Retina Display', 'Retina HD Display',
       'Super Retina XDR Display', 'Full HD+ E3 Super AMOLED Display',
       'Liquid Retina HD Display', 'Quad HD Display', '5G', 'Android',
       'Windows', 'iOS'])))

"""### Support Vector Regression"""

from sklearn.svm import SVR
param_grid = {'C': [0.1, 1, 10, 100, 1000], 
              'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
              'kernel': ['rbf']} 
grid = GridSearchCV(SVR(), param_grid, refit = True, verbose = 3, cv=6)
grid.fit(X_train, y_train)

print(grid.best_params_)
print(grid.best_estimator_)
grid_predictions = grid.predict(X_test)

print("Best Parameters", grid.best_params_)
pred = grid.predict(X_test)
r2 = r2_score(y_test, pred)
print('R2: ', r2)
err = np.sqrt(mean_squared_error(y_test, pred))
print('Root Mean Squared Error: ', err)

# multiple lines with legend
plt.figure(figsize=(23, 9))
plt.plot(np.arange(1,235),y_test,marker='.', color='r', label= 'Actual Value')
plt.plot(np.arange(1,235),pred, marker = '+', color = 'g',label = 'Predicted Value')
plt.xlabel("Index to Mobiles")
plt.ylabel("Actual and Predicted Value")
plt.title("Actual and Predicted Price using SVR")
plt.legend();

grid.best_estimator_.fit_status_

grid.best_estimator_.intercept_

grid.best_estimator_.n_support_

grid.best_estimator_.shape_fit_

grid.best_estimator_.support_vectors_

"""### Catboost Regressor"""

pip install catboost

from catboost import CatBoostRegressor
CBR = CatBoostRegressor()
CBR.get_params()

parameters = {'depth': [6,8,10],
              'learning_rate' : [0.01, 0.05, 0.1],
              'iterations'    : [30, 50, 100]
                 }
grid = GridSearchCV(estimator=CBR, param_grid = parameters, cv = 10, n_jobs=-1)
grid.fit(X_train, y_train)
print("\n The best estimator across ALL searched params:\n", grid.best_estimator_)
print("\n The best score across ALL searched params:\n", grid.best_score_)
print("\n The best parameters across ALL searched params:\n", grid.best_params_)

print(grid.best_params_)
print(grid.best_score_)
pred = grid.predict(X_test)
r2 = r2_score(y_test, pred)
print('R2: ', r2)
err = np.sqrt(mean_squared_error(y_test, pred))
print('Root Mean Squared Error: ', err)

"""### Gradient Tree Boosting"""

from sklearn.ensemble import GradientBoostingRegressor
GBR = GradientBoostingRegressor()
GBR.get_params()

crossvalidation=KFold(n_splits=10,shuffle=True,random_state=1)
search_grid={'n_estimators':[500],'max_depth':[1,2,4],'random_state':[1]}
search=GridSearchCV(estimator=GBR,param_grid=search_grid,scoring='r2',n_jobs=1,cv=crossvalidation)
search.fit(X_train,y_train)

print(search.best_params_)
print(search.best_score_)
pred = search.predict(X_test)
r2 = r2_score(y_test, pred)
print('R2: ', r2)
err = np.sqrt(mean_squared_error(y_test, pred))
print('Root Mean Squared Error: ', err)

# multiple lines with legend
plt.figure(figsize=(23, 9))
plt.plot(np.arange(1,235),y_test,marker='.', color='r', label= 'Actual Value')
plt.plot(np.arange(1,235),pred, marker = '+', color = 'g',label = 'Predicted Value')
plt.xlabel("Index to Mobiles")
plt.ylabel("Actual and Predicted Value")
plt.title("Actual and Predicted Price using GBR")
plt.legend();

GBR = GradientBoostingRegressor()
GBR.fit(X_train, y_train)
pred = GBR.predict(X_test)

importance_gb = GBR.feature_importances_
importance_gb

X_train.columns

columns = X_train.columns
#Combine columns with feature importances
gbGraph = pd.Series(importance_gb, columns)
gbGraph

# Visualizing importance from our model

from matplotlib.pyplot import figure
figure(figsize = (10,10))
gbGraph.sort_values().plot.barh(color='b')
plt.title('Feature Importance')

"""### Conclusion

|Algorithm| R^2         | RMSE        |
|---------| ----------- | ----------- |
|  Random Forest Regressor  |  87.83  |  0.434  |
|  Gradient Tree Boosting  |  86.97  |  0.449 |
|  Cat Boost Regressor  |  86.54  |  0.457  |
|      Decision Tree Regressor    | 82.53   | 0.521       |
|  Support Vector Regressor  |  44.9  |  0.925  |
| Linear Regression         | -2.29      | 1890084119.8       |

## Classification

### Logistic Regression
"""

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, GridSearchCV, StratifiedKFold
import warnings
warnings.filterwarnings('ignore')
log = LogisticRegression()
log.get_params()

#C = [1,2,4]
#fit_intercept = [True, False]
max_iter = [100, 150, 200, 250]
n_jobs = [-1]
#solver = ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']
param_grid = {'n_jobs':n_jobs
             }
grid = GridSearchCV(estimator=log, 
                    param_grid=param_grid, 
                    cv = 10)
grid.fit(X_train, y_train)
from sklearn.metrics import accuracy_score, f1_score
print("Best Parameters", grid.best_params_)
print("Best Parameters", grid.best_score_)

from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
pred = grid.predict(X_test)
accuracy = accuracy_score(y_test, pred)
f1 = f1_score(y_test, pred, average='weighted')
precision = precision_score(y_test, pred, average='weighted')
recall = recall_score(y_test, pred, average='weighted')
print('Accuracy: ', accuracy)
print('F1 Score: ', f1)
print('Precision: ', precision)
print('Recall: ', recall)

"""### KNN"""

from sklearn.neighbors import KNeighborsClassifier
KNN = KNeighborsClassifier()
KNN.get_params()

param_grid = {'algorithm':['auto', 'ball_tree', 'kd_tree', 'brute'],
              'n_neighbors':[4, 5, 7, 9, 10],
              'weights':['uniform', 'distance']
             }
grid = GridSearchCV(estimator=KNN, 
                    param_grid=param_grid, 
                    cv = 10,
                   scoring='accuracy')
grid.fit(X_train, y_train)
print("Best Parameters", grid.best_params_)
print("Best Parameters", grid.best_score_)

from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
pred = grid.predict(X_test)
accuracy = accuracy_score(y_test, pred)
f1 = f1_score(y_test, pred, average='weighted')
precision = precision_score(y_test, pred, average='weighted')
recall = recall_score(y_test, pred, average='weighted')
print('Accuracy: ', accuracy)
print('F1 Score: ', f1)
print('Precision: ', precision)
print('Recall: ', recall)

"""### Naive  Bayes Classifier"""

from sklearn.naive_bayes import GaussianNB
GNB = GaussianNB()
GNB.get_params()

GNB.fit(X_train, y_train)
pred = GNB.predict(X_test)
accuracy = accuracy_score(y_test, pred)
f1 = f1_score(y_test, pred, average='weighted')
precision = precision_score(y_test, pred, average='weighted')
recall = recall_score(y_test, pred, average='weighted')
print('Accuracy: ', accuracy)
print('F1 Score: ', f1)
print('Precision: ', precision)
print('Recall: ', recall)

"""### Desicion Tree Classifier"""

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, GridSearchCV, StratifiedKFold
import warnings
warnings.filterwarnings('ignore')
from sklearn.tree import DecisionTreeClassifier
DTC = DecisionTreeClassifier()
DTC.get_params()

np.any(np.isnan(df1['Price Range']))

param_grid = {'criterion': ['gini', 'entropy', 'log_loss'],
              'splitter': ['best', 'random'],
              'max_depth':[2, 5, 10, 15, 20, 25, 50],
              'max_leaf_nodes':[2, 5, 10, 15, 20, None]
             }
grid = GridSearchCV(estimator=DTC, 
                    param_grid=param_grid, 
                    cv = 9,
                   scoring='accuracy')
grid.fit(X_train, y_train)
from sklearn.metrics import accuracy_score, f1_score
print("Best Parameters", grid.best_params_)
print("Best Parameters", grid.best_score_)

from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
pred = grid.predict(X_test)
accuracy = accuracy_score(y_test, pred)
f1 = f1_score(y_test, pred, average='weighted')
precision = precision_score(y_test, pred, average='weighted')
recall = recall_score(y_test, pred, average='weighted')
print('Accuracy: ', accuracy)
print('F1 Score: ', f1)
print('Precision: ', precision)
print('Recall: ', recall)

"""### Support Vector Machine"""

from sklearn.svm import SVC
SVC = SVC()
SVC.get_params()

SVC.fit(X_train, y_train)
pred = SVC.predict(X_test)
accuracy = accuracy_score(y_test, pred)
f1 = f1_score(y_test, pred, average='weighted')
precision = precision_score(y_test, pred, average='weighted')
recall = recall_score(y_test, pred, average='weighted')
print('Accuracy: ', accuracy)
print('F1 Score: ', f1)
print('Precision: ', precision)
print('Recall: ', recall)

"""### Random Forest Classifier"""

from sklearn.ensemble import RandomForestClassifier
RFC = RandomForestClassifier()
RFC.get_params()

param_grid = {'criterion':['gini', 'entropy', 'log_loss'],
              'max_depth':[20, 25],
              'n_jobs':[-1]
             }
grid = GridSearchCV(estimator=RFC, 
                    param_grid=param_grid, 
                    cv = 8,
                   scoring='accuracy')
grid.fit(X_train, y_train)
print("Best Parameters", grid.best_params_)
print("Best Parameters", grid.best_score_)

from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
pred = grid.predict(X_test)
accuracy = accuracy_score(y_test, pred)
f1 = f1_score(y_test, pred, average='weighted')
precision = precision_score(y_test, pred, average='weighted')
recall = recall_score(y_test, pred, average='weighted')
print('Accuracy: ', accuracy)
print('F1 Score: ', f1)
print('Precision: ', precision)
print('Recall: ', recall)

# multiple lines with legend
plt.figure(figsize=(14, 9))
plt.plot(np.arange(1,235),y_test,marker='.', color='b', label= 'Actual Value')
plt.plot(np.arange(1,235),pred, marker = '+', color = 'g',label = 'Predicted Value')
plt.xlabel("Index to Mobiles")
plt.ylabel("Actual and Predicted Value")
plt.title("Actual and Predicted Price using Random Forest Regressor")
plt.legend();
plt.savefig('Actual and predicted.png')

fig = plt.figure()
plt.figure(figsize=(20,20))
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(np.arange(1,235), y_test)
ax2.plot(np.arange(1,235), pred, 'g')
ax1.set_title("Actual Price")
ax2.set_title("Predicted Price")
plt.xlabel("Index to Mobiles")

a, b = np.polyfit(y_test, pred, 1)
plt.figure(figsize=(14, 9))
plt.plot(y_test, pred,marker='.', color='g')
plt.plot(pred, a*pred+b, 'r') 
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual and Predicted Price")
plt.savefig('Predicted bs actual.png')

"""#### Best Estimator"""

grid.best_estimator_.base_estimator_

grid.best_estimator_.estimators_

grid.best_estimator_.n_features_in_

importance_gb = grid.best_estimator_.feature_importances_
importance_gb

columns = X_train.columns
#Combine columns with feature importances
gbGraph = pd.Series(importance_gb, columns)
gbGraph

# Visualizing importance from our model

from matplotlib.pyplot import figure
figure(figsize = (10,10))
gbGraph.sort_values().plot.barh(color='b')
plt.title('Feature Importance')

len(grid.best_estimator_.estimators_)

# first decision tree of the random forest
grid.best_estimator_.estimators_[0]

#We can plot a first Decision Tree from the Random Forest
from sklearn import tree
plt.figure(figsize=(20,20))
_ = tree.plot_tree(grid.best_estimator_.estimators_[0], feature_names=X_train.columns, filled=True, fontsize=8)
plt.savefig('First Decision Tree.png')

run_classifier(RFR, param_grid, 'Random Forest')

"""# AdaBoost Classifier"""

from sklearn.ensemble import AdaBoostClassifier
ABC = AdaBoostClassifier()
ABC.get_params()

# Commented out IPython magic to ensure Python compatibility.
# %%time
# param_grid = {'n_estimators':[20, 30, 40, 50, 60],
#               'algorithm':['SAMME', 'SAMME.R']
#              }
# grid = GridSearchCV(estimator=ABC, 
#                     param_grid=param_grid, 
#                     cv = 9,
#                    scoring='accuracy')
# grid.fit(X_train, y_train)
# print("Best Parameters", grid.best_params_)
# print("Best Parameters", grid.best_score_)

from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
pred = grid.predict(X_test)
accuracy = accuracy_score(y_test, pred)
f1 = f1_score(y_test, pred, average='weighted')
precision = precision_score(y_test, pred, average='weighted')
recall = recall_score(y_test, pred, average='weighted')
print('Accuracy: ', accuracy)
print('F1 Score: ', f1)
print('Precision: ', precision)
print('Recall: ', recall)

# multiple lines with legend
plt.figure(figsize=(14, 9))
plt.plot(np.arange(1,235),y_test,marker='.', color='b', label= 'Actual Value')
plt.plot(np.arange(1,235),pred, marker = '+', color = 'g',label = 'Predicted Value')
plt.xlabel("Index to Mobiles")
plt.ylabel("Actual and Predicted Value")
plt.title("Actual and Predicted Price using Random Forest Regressor")
plt.legend();
plt.savefig('Actual and predicted.png')

fig = plt.figure()
plt.figure(figsize=(20,20))
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(np.arange(1,235), y_test)
ax2.plot(np.arange(1,235), pred, 'g')
ax1.set_title("Actual Price")
ax2.set_title("Predicted Price")
plt.xlabel("Index to Mobiles")

grid.best_estimator_.base_estimator_

grid.best_estimator_.estimators_

grid.best_estimator_.n_features_in_

importance_gb = grid.best_estimator_.feature_importances_
importance_gb

columns = X_train.columns
#Combine columns with feature importances
gbGraph = pd.Series(importance_gb, columns)
gbGraph

# Visualizing importance from our model

from matplotlib.pyplot import figure
figure(figsize = (10,10))
gbGraph.sort_values().plot.barh(color='b')
plt.title('Feature Importance')

#We can plot a first Decision Tree from the Random Forest
from sklearn import tree
plt.figure(figsize=(20,20))
_ = tree.plot_tree(grid.best_estimator_.estimators_[20], feature_names=X_train.columns, filled=True, fontsize=8)
plt.savefig('First Decision Tree.png')

"""|Algorithm| Accuracy        | 
|---------| ----------- | 
|  Logistic Regression  |  74.35 | 
|  KNN  | 72.64 |  
|  Naive Bayes  |  78.2  |  
|      Decision Tree     | 85.04   | 
|  Random Forest Classifier  |  85.89 |
| Support Vector Machine    | 69.65 |
| Ada Boost Classifier      | 87.6  |

## **DEEP LEARNING**
"""

X = df1.drop(['Price', 'Price Range'],axis=1)
y = df1['Price Range']
from sklearn.preprocessing import LabelEncoder
y = pd.get_dummies(y).values
print(y[0:5])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# import deep learning libraries
import tensorflow as tf
from tensorflow import keras
import keras
#Neural network module
from keras.models import Sequential 
from keras.layers import Dense,Activation,Dropout 
from keras.utils import np_utils

model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(4, activation='softmax')
  ])
model

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, batch_size=50, epochs=10000)

loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print('Test loss:', loss)
print('Test accuracy:', accuracy)
