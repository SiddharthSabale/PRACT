from sklearn import svm

X = [[0], [1], [2], [3]]
y = [0, 1, 2, 3]

clf = svm.SVC(decision_function_shape='ovo')
clf.fit(X, y)

dec = clf.decision_function([[1]])
print(dec)
print(dec.shape[1])  

lin_clf = svm.LinearSVC()
lin_clf.fit(X, y)

dec = lin_clf.decision_function([[1]])
print(dec)
print(dec.shape[0])  
print('svm2')
