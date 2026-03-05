import warnings
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import learning_curve, validation_curve, ShuffleSplit, train_test_split
from sklearn.tree import DecisionTreeRegressor

# Suppress matplotlib user warnings
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")

def ModelComplexity(X, y):
    """ Calculates the performance of the model as model complexity increases. """
    
    # Updated ShuffleSplit syntax (n_splits instead of n_iter)
    # Remove X.shape[0] and change n_iter to n_splits
    cv = ShuffleSplit(n_splits = 10, test_size = 0.2, random_state = 0)

    # Vary the max_depth parameter from 1 to 10
    max_depth = np.arange(1, 11)

    # Use validation_curve directly from sklearn.model_selection
    train_scores, test_scores = validation_curve(
        DecisionTreeRegressor(), X, y, 
        param_name="max_depth", param_range=max_depth, cv=cv, scoring='r2'
    )

    # Calculations for plotting
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)

    # Plotting using 'plt' consistent with your import
    plt.figure(figsize=(7, 5))
    plt.title('Decision Tree Regressor Complexity Performance')
    plt.plot(max_depth, train_mean, 'o-', color='r', label='Training Score')
    plt.plot(max_depth, test_mean, 'o-', color='g', label='Validation Score')
    
    plt.fill_between(max_depth, train_mean - train_std, \
        train_mean + train_std, alpha=0.15, color='r')
    plt.fill_between(max_depth, test_mean - test_std, \
        test_mean + test_std, alpha=0.15, color='g')
    
    plt.legend(loc='lower right')
    plt.xlabel('Maximum Depth')
    plt.ylabel('Score')
    plt.ylim([-0.05, 1.05])
    plt.show()