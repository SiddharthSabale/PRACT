from sklearn import svm
import pandas as pd
data = pd.read_csv('dataset.csv')
print(data.columns)
x = data[['feature1', 'feature2']].values  # Adjust columns to the actual features in your dataset.csv
y = data['target'].values                  # Adjust column to the actual target in your dataset.csv
clf = svm.SVC(decision_function_shape='ovo')
clf.fit(x, y)
sample_input = [[1, 1]]  # Example input data
dec = clf.decision_function(sample_input)
print("\nSVC decision_function output:")
print(dec)
if dec.ndim == 1:
    num_classes = 1
else:
    num_classes = dec.shape[1]
print("Shape of decision_function output (number of classes):")
print(num_classes)
lin_clf = svm.LinearSVC()
lin_clf.fit(x, y)
dec_lin = lin_clf.decision_function(sample_input)
print("\nLinearSVC decision_function output:")
print(dec_lin)
if dec_lin.ndim == 1:
    num_classes_lin = 1
else:
    num_classes_lin = dec_lin.shape[1]

print("Shape of decision_function output for LinearSVC (number of classes):")
print(num_classes_lin)
