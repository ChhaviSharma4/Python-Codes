from sklearn import tree
from sklearn import svm
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

'''to learn about various models'''


x = [[181,80,44],[177,70,43],[160,60,38],[166,65,40],
	[190,90,47],[175,64,39],[177,70,40],[171,75,42],
	[181,85,43]]

y = ['m','f','f','m','m','m','f','f','m']

clf_tree = tree.DecisionTreeClassifier()
clf_tree = clf_tree.fit(x,y)
prediction_tree = clf_tree.predict(x)
acc_tree = accuracy_score(y,prediction_tree)*100
print ("Tree: " ,prediction_tree, acc_tree)

clf_svm = svm.SVC()
clf_svm.fit(x,y)
prediction_svm = clf_svm.predict(x)
acc_svm = accuracy_score(y,prediction_svm)*100
print("SVM: ",prediction_svm,acc_svm)


clf_kernel = SGDClassifier()
clf_kernel.fit(x,y)
prediction_kernel = clf_kernel.predict(x)
acc_kernel = accuracy_score(y,prediction_kernel)*100
print("SGD: ",prediction_kernel, acc_kernel)

clf_knn = KNeighborsClassifier()
clf_knn.fit(x,y)
prediction_knn = clf_knn.predict(x)
acc_knn = accuracy_score(y,prediction_knn)*100
print("KNN: ",prediction_knn, acc_knn)


clf_perceptron = Perceptron()
clf_perceptron.fit(x,y)
prediction_perceptron = clf_perceptron.predict(x)
acc_perceptron = accuracy_score(y,prediction_perceptron)*100
print("KNN: ",prediction_perceptron, acc_perceptron)


dictionary = {'Tree':acc_tree,'SVM':acc_svm,'SGD':acc_kernel,
				'KNN':acc_knn,'Perceptron':acc_perceptron}
'''maximum = max(dictionary.values())'''
#gives the value of key
maximum = max(dictionary, key= lambda i:dictionary[i])
print(maximum, dictionary[maximum])
#for key in dictionary:
#	print(key in dictionary[maximum])
print('The best gender classifier is {} with accuracy {}'
	.format(maximum,dictionary[maximum]))

