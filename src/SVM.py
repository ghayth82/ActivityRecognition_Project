import pandas as pd
from sklearn.preprocessing import normalize
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import normalize
import warnings
warnings.filterwarnings('ignore')
from sklearn import preprocessing
import glob
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import itertools

#Divide the data into training and testing
X_train = pd.read_csv('F:\\Capsense_Stan\\RLSTools\\data\\band\\demo_patient0\\training_data\\training_data.csv')
Y_train = pd.read_csv('F:\\Capsense_Stan\\RLSTools\\data\\band\\demo_patient0\\training_data\\training_labels.csv',header=None)
X_train = X_train.fillna(0)
Y_train = Y_train.fillna(0)
X_train = X_train.astype('int')
Y_train = Y_train.astype('int')


#X_train, X_test, y_train, y_test = train_test_split(total_data, total_label, test_size=0.10, random_state=1)
X_test = pd.read_csv('F:\\Capsense_Stan\\RLSTools\\data\\band\\demo_patient0\\testing_data\\testing_data.csv')
Y_test = pd.read_csv('F:\\Capsense_Stan\\RLSTools\\data\\band\\demo_patient0\\testing_data\\testing_labels.csv',header=None)
X_test = X_test.fillna(0)
Y_test = Y_test.fillna(0)
X_test = X_test.astype('int')
Y_test = Y_test.astype('int')

print("Dimensions of train data ")
print(X_train.shape)
print("Dimensions of training labels ")
print(Y_train.shape)
print("Dimensions of test data ")
print(X_test.shape)
print("Dimensions of test labels ")
print(Y_test.shape)

#Testing consist of one minute session of each activity; activity is performed in a continuous manner
print(" --------------Training SVC (One vs Rest)in svm ------------------------")
class_names = ['kicking','fidgeting','rubbing','crossing','gas_pedal','streching','idle']
classifier = svm.SVC(decision_function_shape="ovr", kernel= "poly", random_state=1)
classifier.fit(X_train, Y_train)

print("------------------------ Testing the model-----------------------------")
label_predicted = classifier.predict(X_test)

accuracy = accuracy_score(Y_test, label_predicted)

print("Test Accuracy ")
print(accuracy * 100)

cnf_matrix = confusion_matrix(Y_test, label_predicted)
np.set_printoptions(precision=2)

plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names, normalize=True,
                      title='Normalized confusion matrix')
plt.show()
