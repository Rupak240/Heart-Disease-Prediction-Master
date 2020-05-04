
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Importing the dataset
dataset = pd.read_csv('C:/Users/rupak dey/Desktop/Heart-disease-prediction-master/Heart-disease-prediction-master/predict_risk/machine_learning_models/HealthData.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:, 13].values
#handling missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer=imputer.fit(X[:,11:13])
X[:,11:13]=imputer.transform(X[:,11:13])
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 3)
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#saving StandardScaler file in pickle
from joblib import dump, load
dump(sc,'C:/Users/rupak dey/Desktop/Heart-disease-prediction-master/Heart-disease-prediction-master/predict_risk/production/std_scaler1.pkl', compress=True)
# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)
#Saving the model in pickle
import joblib
filename = 'C:/Users/rupak dey/Desktop/Heart-disease-prediction-master/Heart-disease-prediction-master/predict_risk/production/naive_bayes_model.pkl'
joblib.dump(classifier,filename)

# Predicting the Test set results
y_pred = classifier.predict(X_test)
#ACCURACY SCORE
from sklearn.metrics import accuracy_score
yp = accuracy_score(y_test,y_pred)
print(yp)
# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
#Interpretation:
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
