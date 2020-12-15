'''
Dealing with missing Data
'''
import pandas as pd
import numpy as np
'''
Step 1: Check for missing data
''' 
df = pd.DataFrame({'x':[8,9,np.nan], 'y':[np.nan,'c',np.nan], 'z':[1,2,3]})

#-- How many rows have missing values for each of the fields
df.isnull().sum()
# axis parameter is set to 0 by default
df.isnull().sum(axis = 0) 

#-- How many fields are missing in each row 
df.isnull().sum(axis = 1) 

'''
Now that the fields with missing values are known, 
they could be dealt with in 2 possible ways: -
a. Remove the data-points or rows with missing data
    - Not recommended unless very few data points show missing values
    - There might be a pattern to missing values which will be lost if all
      data points with missing values are dropped
b. Fill the missing values by a suitable value chosen based on the nature of data and problem at hand
    - Mean
    - Median
    - Mode
    - Some text indicting the value here was missing in case of categorical fields
    - A constant value like 0 (in some cases, null value just means zero value)
    - Impute with a value that is the result of a regression model that is trained on data points without a missing value
      and that uses other non-null fields of the data point 
'''

#-- Dropping rows with na
df_without_nulls = df.dropna()

#-- Replace null values by a value
df_na_replaced = df.fillna(0)
df_na_replaced_specific = df.fillna({'x':99, 'y':22, 'z':45})

#-- Iterative Imputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
num_cols = [col1, col2, col3, col4, col5]
imputer = impute.IterativeImputer()
imputed = imputer.fit_transform(
        X_train[num_cols]
        )
X_train.loc[:, num_cols] = imputed
imputed = imputer.transform(X_test[num_cols])
X_test.loc[:,num_cols] = imputed
