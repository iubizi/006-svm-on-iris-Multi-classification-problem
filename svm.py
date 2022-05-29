import gc
gc.enable()

####################
# load iris
####################

from sklearn.datasets import load_iris
iris = load_iris()

x = iris.data
y = iris.target

# Turn the problem into a binary classification problem
x = x[y!=2]
y = y[y!=2]

####################
# train test split
####################

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.33, random_state=42, stratify=y)

####################
# svm with dump
####################

from sklearn import svm
import joblib # saving model

model = svm.SVC() # linear svm
model.fit(x_train, y_train)

# save model
joblib.dump(model, 'svm.dump')

# Load the saved model (the usage of dump is demonstrated here)
model = joblib.load('svm.dump')

y_pred = model.predict(x_test)
print(y_test) # see the difference
print(y_pred)
print()

####################
# confusion matrix
####################

from sklearn.metrics import confusion_matrix

tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

print('confusion matrix')
print('='*15)
print('tp =', tp, end=' | '); print('fp =', fp)
print('-'*20)
print('fn =', fn, end=' | '); print('tn =', tn)

'''
[1 0 1 0 0 0 0 0 0 1 1 0 1 1 0 1 1 0 0 0 1 1 0 0 1 1 0 1 1 0 1 1 0]
[1 0 1 0 0 0 0 0 0 1 1 0 1 1 0 1 1 0 0 0 1 1 0 0 1 1 0 1 1 0 1 1 0]

confusion matrix
===============
tp = 16 | fp = 0
--------------------
fn = 0 | tn = 17
'''
