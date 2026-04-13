# data_utils.py

import pandas as pd
import numpy as np

def prepare_features_and_target(data):
    """
    Converts sklearn dataset to DataFrame and extracts features and target.

    Parameters:
        data: sklearn.utils.Bunch
            A dataset object with 'data', 'target', and 'feature_names'.

    Returns:
        X: np.ndarray
            Features as a NumPy array.
        y: np.ndarray
            Target as a NumPy array.
    """
    df = pd.DataFrame(data=data['data'], columns=data.feature_names)
    df['target'] = data['target']

    X = df.iloc[:, :-1].values
    y = df['target'].values

    return X, y
