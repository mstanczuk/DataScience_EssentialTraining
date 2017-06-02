import numpy as np
import pandas as pd

from pandas import Series, DataFrame

#Removing Duplicates
DF_obj = DataFrame({'column 1': [1, 1, 2, 2, 3, 3, 3],
                    'column 2' : ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
                    'column 3' : ['A', 'A', 'B', 'B', 'C', 'C', 'C']})
print(DF_obj)
print('')

print(DF_obj.duplicated())
print('')

print (DF_obj.drop_duplicates())
print('')

DF_obj = DataFrame({'column 1': [1, 1, 2, 2, 3, 3, 3],
                    'column 2' : ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
                    'column 3' : ['A', 'A', 'B', 'B', 'C', 'D', 'C']})
print('')
print(DF_obj.drop_duplicates(['column 3']))