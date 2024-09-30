import numpy as np

# Load dataset from CSV
data = np.genfromtxt('dataset.csv', delimiter=',', skip_header=1)
X = data[:, :2]  # Input features
Y = data[:, 2].reshape(-1, 1)  # Target output

# Neural network parameters and initialization
weights = np.random.rand(2, 1)  # Initialize weights for 2 input features and 1 output neuron
bias = np.random.rand()  # Initialize bias
lr = 0.05  # Learning rate

# Activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_der(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Training loop
epochs = 1000
for epoch in range(epochs):
    # Forward pass
    in_0 = np.dot(X, weights) + bias
    out_0 = sigmoid(in_0)

    # Calculate error
    error = out_0 - Y

    # Backpropagation
    derror_douto = error
    douto_dino = sigmoid_der(out_0)
    deriv = derror_douto * douto_dino
    inputs_T = X.T
    deriv_final = np.dot(inputs_T, deriv)

    # Update weights and bias
    weights -= lr * deriv_final
    bias -= lr * np.sum(deriv)

# Testing with a new input
new_input = np.array([[0.7, 0.8]])
result = sigmoid(np.dot(new_input, weights) + bias)
print(result)
