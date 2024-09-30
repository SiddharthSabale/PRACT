import numpy as np

input_features = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

print(input_features.shape)
print(input_features)

target_output = np.array([[0], [1], [1], [1]])
print(target_output.shape)
print(target_output)

weights = np.array([[0.1, 0.2], [0.3, 0.4]])
print(weights.shape)
print(weights)

bias = 0.3
lr = 0.05

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_der(x):
    return sigmoid(x) * (1 - sigmoid(x))

inputs = input_features
in_0 = np.dot(inputs, weights) + bias
out_0 = sigmoid(in_0)

error = out_0 - target_output
x = error.sum()
print(x)

derror_douto = error
douto_dino = sigmoid_der(out_0)
deriv = derror_douto * douto_dino
inputs_T = input_features.T
deriv_final = np.dot(inputs_T, deriv)

weights -= lr * deriv_final

for i in deriv:
    bias -= lr * i.sum()

single_point = np.array([1, 0])
result_1 = np.dot(single_point, weights) + bias
result_2 = sigmoid(result_1)

print(result_2)
