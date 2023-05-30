import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data, iris.target
clf = tree.DecisionTreeClassifier(max_depth=4)
clf = clf.fit(x, y)
plt.figure(figsize=(12,8))
tree.plot_tree(clf, filled=True, fontsize=10)
plt.show()
