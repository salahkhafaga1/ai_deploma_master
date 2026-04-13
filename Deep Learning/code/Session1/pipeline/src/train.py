from data import prepare_features_and_target
import pandas as pd 
import numpy as np
from perceptron import *
from activation import sigmoid
from tqdm import tqdm
from eval import accuarcy
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split 
import warnings  
warnings.filterwarnings('ignore')
data=load_breast_cancer()
X, y = prepare_features_and_target(data)
train_X,test_X,train_y,test_y=train_test_split(X,y,test_size=0.2)
lr=0.001
weights=np.zeros(train_X.shape[1]) #30 zero for 30 weight
bais=0
for i in tqdm(range(10000), desc="Training"):
    pred = perceptron(train_X, weights, bais)
    weights = update_weights(weights, train_X, pred, train_y, lr)
    bais = update_bais(bais, train_X, pred, train_y, lr)
y_pred=perceptron(test_X,weights,bais)
print("Test_Accuarcy : " ,accuarcy(y_pred,test_y))
y_pred=perceptron(train_X,weights,bais)
print("Train_Accuarcy : " ,accuarcy(y_pred,train_y))