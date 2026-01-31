import pandas as pd
import numpy as np

def isnull_count(df):
    null = df.isnull()
    return pd.DataFrame(null).T

# isnull_count(df)
df = pd.DataFrame({'A': [1, None, 3], 'B': [None, 5, 6]})
isnull_count(df)
# ------------------
def chk_type(df):
    dtypes=df.dtypes
    n_unique=df.nunique()
    return pd.DataFrame({'dtypes':dtypes,'n_unique':n_unique}).T
chk_type(df)
# ------------------
cols=['A','B']
def convert_to_category(cols):
    df[cols] = df[cols].astype('category')
    
    
convert_to_category(cols)
# ------------------
vec=np.array([1,2,3,4,5,6])
def reshape_vector_to_matrix(vec):
    return vec.reshape(2,3)
reshape_vector_to_matrix(vec)