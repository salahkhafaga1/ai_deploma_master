import numpy as np
def accuarcy(y_pred,y_actual):
    return np.sum(y_pred==y_actual)/len(y_actual)