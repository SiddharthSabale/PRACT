import pandas as pd
from sklearn import model_selection
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(url, names=names)

X = dataframe.drop('class', axis=1)
Y = dataframe['class']

seed = 7
kfold = model_selection.KFold(n_splits=10, shuffle=True, random_state=seed)

models = []
models.append(('DecisionTree', DecisionTreeClassifier(random_state=seed)))
models.append(('KNN', KNeighborsClassifier()))
models.append(('SVM', SVC(random_state=seed)))

voting_model = VotingClassifier(estimators=models, voting='hard')

results = model_selection.cross_val_score(voting_model, X, Y, cv=kfold)
print("Accuracy:", results.mean())
