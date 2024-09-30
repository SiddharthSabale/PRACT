
from sklearn import svm
import pandas as pd
# Load data from CSV using pandas
data = pd.read_csv('dataset.csv')
x = data[['feature1', 'feature2']].values
y = data['target'].values
clf = svm.SVC()
clf.fit(x, y)

print(clf.predict([[2, 2]]))
print(clf.support_vectors_)
print(clf.support_)
print(clf.n_support_)
