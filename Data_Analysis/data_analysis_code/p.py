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
# ---------------

import numpy as np

def array_factory(mode, shape, value=None):
    """
    Creates various NumPy arrays based on the mode.
    """
    try:
        if mode == "zeros":
            return np.zeros(shape)
        elif mode == "ones":
            return np.ones(shape)
        elif mode == "full":
            if value is None:
                raise ValueError("Mode 'full' requires a 'value' parameter.")
            return np.full(shape, value)
        elif mode == "identity":
            size = shape[0] if isinstance(shape, (list, tuple)) else shape
            return np.eye(size)
        else:
            return "please enter the correct mode"
            
    except Exception as e:
        return str(e)

