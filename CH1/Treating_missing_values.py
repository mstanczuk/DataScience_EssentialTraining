import numpy as np
import pandas as pd

from pandas import Series, DataFrame

missing = np.nan
series_obj = Series(['row 1', 'row 2', missing, 'row 4', 'row 5', 'row 6', missing, 'row 8'])
print(series_obj)

#Identyfing missing values
print('')
print(series_obj.isnull())

#Filling in for missing values
np.random.seed(25)
DF_obj = DataFrame(np.random.randn(36).reshape(6,6))
print('')
print(DF_obj)

DF_obj.ix[3:5, 0] = missing
DF_obj.ix[1:4, 5] = missing
print ('')
print (DF_obj)

filled_DF=DF_obj.fillna(0) #fill in missing values with given value
print('')
print (filled_DF)

filled_DF=DF_obj.fillna({0: 0.1, 5: 1.25}) #fill in missing values with given value foe every given column
print('')
print(filled_DF)

filled_DF=DF_obj.fillna(method='ffill') #fills missing values with last encountered value in column
print('')
print(filled_DF)

#Counting missing values
print('')
print(DF_obj.isnull().sum())

#Filtering out missing values
DF_no_NaN = DF_obj.dropna() #drop every  that have missing value in it
print('')
print(DF_no_NaN)

DF_no_NaN_col = DF_obj.dropna(axis=1) #drop every  that have missing value in it
print('')
print(DF_no_NaN_col)

print('')
print(DF_obj.dropna(how='all')) #drop only rows with all missing values
