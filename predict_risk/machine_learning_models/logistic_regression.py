
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Importing the dataset
#DIR='C:/Users/Mansi/Desktop/Heart_disease_prediction_project/predict_risk/machine_learning_models'

dataset = pd.read_csv('C:/Users/rupak dey/Desktop/Heart-disease-prediction-master/Heart-disease-prediction-master/predict_risk/machine_learning_models/HealthData.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 13].values
#handling missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer=imputer.fit(X[:,11:13])
X[:,11:13]=imputer.transform(X[:,11:13])

#splitting dataset into training set and test set

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.20,random_state=5)
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)
#Saving StandardScaler into pickle
from joblib import dump, load
dump(sc_X,'C:/Users/rupak dey/Desktop/Heart-disease-prediction-master/Heart-disease-prediction-master/predict_risk/production/std_scaler2.pkl', compress=True)
### logistic regression

#fitting LR to training set

from sklearn.linear_model import LogisticRegression
classifier =LogisticRegression(random_state=8)
classifier.fit(X_train,Y_train)

#Saving the model to disk
import joblib

filename = 'C:/Users/rupak dey/Desktop/Heart-disease-prediction-master/Heart-disease-prediction-master/predict_risk/production/Logistic_regression_model.pkl'
joblib.dump(classifier,filename)
#Predict the test set results

y_Class_pred=classifier.predict(X_test)
#checking the accuracy for predicted results

from sklearn.metrics import accuracy_score
yp = accuracy_score(Y_test,y_Class_pred)
print(yp)
# Making the Confusion Matrix

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, y_Class_pred)
#Interpretation:

from sklearn.metrics import classification_report
print(classification_report(Y_test, y_Class_pred))
