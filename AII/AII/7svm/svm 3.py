
from sklearn import svm
import pandas as pd

# Load data from CSV using pandas
data = pd.read_csv('dataset.csv')

# Assuming 'dataset.csv' has columns 'feature1', 'feature2', and 'target'
# Adjust column names as per your actual dataset
x = data[['feature1', 'feature2']].values
y = data['target'].values

# Create SVM classifier
clf = svm.SVC()
clf.fit(x, y)

# Example prediction
print(clf.predict([[2, 2]]))

# Print support vectors
print(clf.support_vectors_)

# Indices of support vectors
print(clf.support_)

# Number of support vectors for each class
print(clf.n_support_)
