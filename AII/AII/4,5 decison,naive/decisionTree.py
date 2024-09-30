import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
import matplotlib.pyplot as plt

iris = load_iris()

print(iris.target_names)
removed=[0,50,100]
new_target=np.delete(iris.target,removed)
new_data=np.delete(iris.data,removed,axis=0)

clf=tree.DecisionTreeClassifier()
clf=clf.fit(new_data,new_target)
prediction=clf.predict(iris.data[removed])

print("original labels:",iris.target[removed])
print("labels predicted:",prediction)

tree.plot_tree(clf)
plt.show()
