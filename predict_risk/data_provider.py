import os
import klepto
import pickle, gzip
import joblib

config = {
    'heart': {
        'SVC': 'production/svc_model.pkl',
        'LogisticRegression': 'production/Logistic_regression_model.pkl',
        'NaiveBayes': 'production/naive_bayes_model.pkl',
        'DecisionTree':'production/decision_tree_model.pkl',
        'Boost':'production/xgboost.pkl',
        'RandomForest':'production/random_forest_model.pkl',
        'scaler_file1': 'production/std_scaler1.pkl',
        'scaler_file2': 'production/std_scaler2.pkl',
        'scaler_file3':'production/std_scaler3.pkl',

    }}

dir = os.path.dirname(__file__)

def GetJobLibFile(filepath):
    if os.path.isfile(os.path.join(dir, filepath)):
        return joblib.load(os.path.join(dir, filepath))
    return None

def GetPickleFile(filepath):
    if os.path.isfile(os.path.join(dir, filepath)):
        return joblib.load( open(os.path.join(dir, filepath), "rb" ) )
    else:
        return None

def GetStandardScalarForHeart1():
    return GetPickleFile(config['heart']['scaler_file1'])

def GetStandardScalarForHeart2():
    return GetPickleFile(config['heart']['scaler_file2'])

def GetStandardScalarForHeart3():
    return GetPickleFile(config['heart']['scaler_file3'])

def GetSVCClassifierForHeart():
    return GetJobLibFile(config['heart']['SVC'])

def GetLogisticRegressionClassifierForHeart():
    return GetJobLibFile(config['heart']['LogisticRegression'])

def GetNaiveBayesClassifierForHeart():
    return GetJobLibFile(config['heart']['NaiveBayes'])

def GetDecisionTreeClassifierForHeart():
    return GetJobLibFile(config['heart']['DecisionTree'])

def GetXgboostForHeart():
    return GetJobLibFile(config['heart']['Boost'])

def GetRandomForestClassifierForHeart():
    return GetJobLibFile(config['heart']['RandomForest'])

def GetAllClassifiersForHeart():
    return (GetSVCClassifierForHeart(),GetLogisticRegressionClassifierForHeart(),GetNaiveBayesClassifierForHeart(),GetDecisionTreeClassifierForHeart(),GetXgboostForHeart(),GetRandomForestClassifierForHeart())
