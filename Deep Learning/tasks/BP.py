import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# input data and expected output
X = np.array([[0.05, 0.10]])
y = np.array([[0.01, 0.99]])
# intial weights and biases
w1, w2, w3, w4 = 0.15, 0.20, 0.25, 0.30
w5, w6, w7, w8 = 0.40, 0.45, 0.50, 0.55
b1, b2 = 0.35, 0.60
# convert weights to numpy arrays for easier calculations
weights_hidden = np.array([[w1, w3], [w2, w4]])
weights_output = np.array([[w5, w7], [w6, w8]])

learning_rate = 0.5

for i in range(10001):
    # Forward Pass
    hidden_layer_input = np.dot(X, weights_hidden) + b1
    hidden_layer_output = sigmoid(hidden_layer_input)
    
    output_layer_input = np.dot(hidden_layer_output, weights_output) + b2
    predicted_output = sigmoid(output_layer_input)
    # determine the error
    error = 0.5 * np.sum((y - predicted_output)**2)
    
    # Backpropagation
    d_predicted_output = (predicted_output - y) * sigmoid_derivative(predicted_output)
    
    error_hidden_layer = d_predicted_output.dot(weights_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)
    
    # Update weights
    weights_output -= hidden_layer_output.T.dot(d_predicted_output) * learning_rate
    weights_hidden -= X.T.dot(d_hidden_layer) * learning_rate

    if i % 1000 == 0:
        print(f"Iteration {i} Error: {error:.8f}")

print("\nFinal Prediction after 10,000 iterations:")
print(predicted_output)