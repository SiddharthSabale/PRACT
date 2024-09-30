import numpy as np

data = np.genfromtxt('dataset.csv', delimiter=',', skip_header=1)
X = data[:, :2]
Y = data[:, 2].reshape(-1, 1)

weights = np.random.rand(2, 1)
bias = np.random.rand()
lr = 0.05

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_der(x):
    return sigmoid(x) * (1 - sigmoid(x))

epochs = 1000
for epoch in range(epochs):
    in_0 = np.dot(X, weights) + bias
    out_0 = sigmoid(in_0)

    error = out_0 - Y

    derror_douto = error
    douto_dino = sigmoid_der(out_0)
    deriv = derror_douto * douto_dino
    inputs_T = X.T
    deriv_final = np.dot(inputs_T, deriv)

    weights -= lr * deriv_final
    bias -= lr * np.sum(deriv)

new_input = np.array([[0.7, 0.8]])
result = sigmoid(np.dot(new_input, weights) + bias)
print(result)
