import numpy as np
import pandas as pd

from pandas import Series, DataFrame

DF_obj = pd.DataFrame(np.arange(36).reshape(6,6))
print(DF_obj)
print('')

DF_obj_2 = pd.DataFrame(np.arange(15).reshape(5,3))
print(DF_obj_2)
print('')

#Concatenating Data
print(pd.concat([DF_obj, DF_obj_2], axis=1))
print('')

print(pd.concat([DF_obj, DF_obj_2]))
print('')

#Droping values
print(DF_obj.drop([0,2]))
print('')
print(DF_obj.drop([0,2], axis=1))
print('')

#Adding data
series_obj = Series(np.arange(6))
series_obj.name='added_variable'
print(series_obj)
print('')

variable_added = DataFrame.join(DF_obj, series_obj) #add new row
print(variable_added)
print('')

added_datatable = variable_added.append(variable_added, ignore_index=False) #add to bottom of data
print(added_datatable)
print('')

added_datatable = variable_added.append(variable_added, ignore_index=True) #add to bottom of data
print(added_datatable)
print('')

#Sorting data
DF_sorted = DF_obj.sort_values(by=[5], ascending=[False])
print(DF_sorted)