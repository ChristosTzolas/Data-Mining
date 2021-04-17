<<<<<<< Updated upstream
=======
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#libraries
import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt 
import seaborn as sns
sns.set(style='darkgrid')
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score,precision_score,recall_score
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression


# %%
from sklearn.metrics import accuracy_score


# %%
df = pd.read_csv('healthcare-dataset-stroke-data.csv')
df.head()


# %%
len(df)


# %%
df.isnull().sum()


# %%
df[df == 'Unknown']


# %%
#So we have missing values in 'bmi' column and some 'unknown' values in smoking_status
#Drop only missing values
df1a = df.drop(columns = ['bmi'])


# %%
df1a.head()


# %%
#Drop missing values and "Unknown" values
#First Matrix
df1b = df.drop(columns = ['bmi','smoking_status'])
df1b.head()


# %%



# %%
#Mean Imputation


# %%
df2 = df.copy()


# %%
df2.head()


# %%
df2['bmi'].isnull().sum()


# %%
#Mean of bmi column
np.mean(df2.bmi)


# %%
#fill N/A values with mean value
df2['bmi'].fillna(np.mean(df2.bmi), inplace=True)


# %%
#Second Matrix
df2.head()


# %%
#Checking if missing values still exists
df2.bmi.isnull().sum()


# %%
def onehot_encode(dff, column):
    dff = dff.copy()
    dummies = pd.get_dummies(dff[column], prefix = column) 
    dff = pd.concat([dff, dummies], axis=1)#Side by side (axis=1)
    dff = dff.drop(column, axis=1)
    return dff


# %%
def preprocess_inputs(dff):
    dff = dff.copy()
    #Drop id column because its not needed
    dff = dff.drop('id', axis =1)

    #Binary encoding
    dff['ever_married'] = dff['ever_married'].replace({'No': 0,'Yes':1})
    dff['Residence_type'] = dff['Residence_type'].replace({'Rural': 0,'Urban':1})

    #One-Hot encoding
    for column in ['gender', 'work_type', 'smoking_status']:
        dff= onehot_encode(dff, column=column)

    #Split dff
    y= dff['stroke']
    X= dff.drop('stroke',axis=1) 

    #Train_Test_Split
    X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=0.75, shuffle=True, random_state=1)
    
    #KNN imputation
    imputer = KNNImputer()
    imputer.fit(X_train)
    X_train = pd.DataFrame(imputer.transform(X_train), index=X_train.index, columns=X_train.columns)
    X_test = pd.DataFrame(imputer.transform(X_test), index=X_test.index, columns=X_test.columns)

    #Scale X
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = pd.DataFrame(scaler.transform(X_train), index=X_train.index, columns=X_train.columns)
    X_test = pd.DataFrame(scaler.transform(X_test), index=X_test.index, columns=X_test.columns)
        
    return  X_train, X_test, y_train, y_test


# %%
X_train, X_test, y_train, y_test = preprocess_inputs(df)


# %%
X_train
#Before Scaling


# %%
X_train
#After Scaling


# %%
X_train.mean()
#Close to 0


# %%
X_train.var()
#Close to 1
#The 0 at "gender_other" happened because of OneHot encoding


# %%
X_test
#before Scaling


# %%
X_test


# %%
X_train.isna().sum()


# %%
X_test.isna().sum()


# %%
y_train


# %%
y_test


# %%
{column: len(X[column].unique())for column in X.select_dtypes('object').columns}
#We will use binary encoding for ever_married and Residence_type because of the 2 different values
#We will use OneHote Encoding for the rest


# %%
#For the OneHote econding Example
pd.get_dummies(X['work_type'],prefix='work_type')


# %%



>>>>>>> Stashed changes
