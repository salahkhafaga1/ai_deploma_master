import numpy as np
from activation import sigmoid
def update_weights(weights,X,z,y,lr):
    m=len(y)
    
    dw=(1/m)*np.dot(X.T,(z-y))
    
    weights=weights-lr*dw
    
    return weights
def update_bais(bais,X,z,y,lr):
    m=len(y)
    
    db=(1/m)*np.sum(z-y)
    bais=bais-lr*db
    return bais
def perceptron(X,weights,bais):
    z=np.dot(X,weights)+bais
    
    y_pred=sigmoid(z)
    
    y_p=[1 if y>=0.5 else 0  for y in y_pred ]
     
    """ 
    y_p=[]
    for y in y_pred:
        if y>=0.5:
            y_p.append(1)
            
        else:
            y_p.append(0)
            
    """

    return y_p