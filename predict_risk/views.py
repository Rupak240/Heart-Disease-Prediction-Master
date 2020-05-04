import csv,io
from django.shortcuts import render, get_object_or_404, redirect, render
from .forms import Predict_Form
from predict_risk.data_provider import *
from accounts.models import UserProfileInfo
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required,permission_required
from django.urls import reverse
from django.contrib import messages

@login_required(login_url='/')
def PredictRisk(request,pk):
    predicted = False
    predictions={}
    if request.session.has_key('user_id'):
        u_id = request.session['user_id']

    if request.method == 'POST':
        form = Predict_Form(data=request.POST)
        profile = get_object_or_404(UserProfileInfo, pk=pk)

        if form.is_valid():
            features = [[ form.cleaned_data['age'], form.cleaned_data['sex'], form.cleaned_data['cp'], form.cleaned_data['resting_bp'], form.cleaned_data['serum_cholesterol'],
            form.cleaned_data['fasting_blood_sugar'], form.cleaned_data['resting_ecg'], form.cleaned_data['max_heart_rate'], form.cleaned_data['exercise_induced_angina'],
            form.cleaned_data['st_depression'], form.cleaned_data['st_slope'], form.cleaned_data['number_of_vessels'], form.cleaned_data['thallium_scan_results']]]


            standard_scalar1 = GetStandardScalarForHeart1()
            standard_scalar2 = GetStandardScalarForHeart2()
            standard_scalar3 = GetStandardScalarForHeart3()
            features1 = standard_scalar1.transform(features)
            features2= standard_scalar2.transform(features)
            features3= standard_scalar3.transform(features)
            SVCClassifier,LogisticRegressionClassifier,NaiveBayesClassifier,DecisionTreeClassifier,XgboostClassifier,RandomForestClassifier=GetAllClassifiersForHeart()


            predictions = {'SVC': str(SVCClassifier.predict(features2)[0]),
            'LogisticRegression': str(LogisticRegressionClassifier.predict(features2)[0]),
             'NaiveBayes': str(NaiveBayesClassifier.predict(features1)[0]),
             'DecisionTree': str(DecisionTreeClassifier.predict(features1)[0]),
             'Boostxg': str(XgboostClassifier.predict(features3)[0]),
             'RandomForest': str(RandomForestClassifier.predict(features3)[0]),
              }

            pred = form.save(commit=False)

            l=[predictions['SVC'],predictions['LogisticRegression'],predictions['NaiveBayes'],predictions['DecisionTree'],predictions['Boostxg'],predictions['RandomForest']]
            count=l.count('1')

            result=False

            if count>=3:
                result=True
                pred.num=1
            else:
                pred.num=0

            pred.profile = profile

            pred.save()
            predicted = True

            colors={}

            if predictions['SVC']=='0':
                colors['SVC']="table-success"
            elif predictions['SVC']=='1':
                colors['SVC']="table-danger"

            if predictions['LogisticRegression']=='0':
                colors['LR']="table-success"
            else:
                colors['LR']="table-danger"

            if predictions['NaiveBayes']=='0':
                colors['NB']="table-success"
            else:
                colors['NB']="table-danger"

            if predictions['DecisionTree']=='0':
                colors['DT']="table-success"
            else:
                colors['DT']="table-danger"

            if predictions['Boostxg']=='0':
                colors['XGB']="table-success"
            else:
                colors['XGB']="table-danger"

            if predictions['RandomForest']=='0':
                colors['RF']="table-success"
            else:
                colors['RF']="table-danger"


    if predicted:
        return render(request, 'predict.html',
                      {'form': form,'predicted': predicted,'user_id':u_id,'predictions':predictions,'result':result,'colors':colors})

    else:
        form = Predict_Form()

        return render(request, 'predict.html',
                      {'form': form,'predicted': predicted,'user_id':u_id,'predictions':predictions})






















































#
#         if ((SVCClassifier.predict(features2)[0]) == 0):
#             svc = "NEGATIVE"
#         else:
#             svc = "POSITIVE"
#
#         if ((LogisticRegressionClassifier.predict(features2)[0]) == 0):
#             lr = "NEGATIVE"
#         else:
#             lr = "POSITIVE"
#
#         if ((NaiveBayesClassifier.predict(features1)[0]) == 0):
#             nb = "NEGATIVE"
#         else:
#             nb = "POSITIVE"
#
#         if ((DecisionTreeClassifier.predict(features1)[0]) == 0):
#             dt = "NEGATIVE"
#         else:
#             dt = "POSITIVE"
#
#         if ((XgboostClassifier.predict(features3)[0]) == 0):
#             xb = "NEGATIVE"
#         else:
#             xb = "POSITIVE"
#
#         if ((RandomForestClassifier.predict(features3)[0]) == 0):
#             rf = "NEGATIVE"
#         else:
#             rf = "POSITIVE"
#
#
#         predictions = {'SVC': svc,
#         'LogisticRegression': lr,
#          'NaiveBayes': nb,
#          'DecisionTree': dt,
#          'Boostxg': xb,
#          'RandomForest': rf,
#           }
#
#
#         pred = form.save(commit=False)
#
#         l=[predictions['SVC'],predictions['LogisticRegression'],predictions['NaiveBayes'],predictions['DecisionTree'],predictions['Boostxg'],predictions['RandomForest']]
#         count=l.count('POSITIVE')
#
#         result=False
#
#         if count>=3:
#             result=True
#             pred.num=1
#         else:
#             pred.num=0
#
#         pred.profile = profile
#
#         pred.save()
#         predicted = True
#
#         colors={}
#
#         if predictions['SVC']=='NEGATIVE':
#             colors['SVC']="table-success"
#         elif predictions['SVC']=='POSITIVE':
#             colors['SVC']="table-danger"
#
#         if predictions['LogisticRegression']=='NEGATIVE':
#             colors['LR']="table-success"
#         else:
#             colors['LR']="table-danger"
#
#         if predictions['NaiveBayes']=='NEGATIVE':
#             colors['NB']="table-success"
#         else:
#             colors['NB']="table-danger"
#
#         if predictions['DecisionTree']=='NEGATIVE':
#             colors['DT']="table-success"
#         else:
#             colors['DT']="table-danger"
#
#         if predictions['Boostxg']=='NEGATIVE':
#             colors['XGB']="table-success"
#         else:
#             colors['XGB']="table-danger"
#
#         if predictions['RandomForest']=='NEGATIVE':
#             colors['RF']="table-success"
#         else:
#             colors['RF']="table-danger"
#
#
# if predicted:
#     return render(request, 'predict.html',
#                   {'form': form,'predicted': predicted,'user_id':u_id,'predictions':predictions,'result':result,'colors':colors})
#
# else:
#     form = Predict_Form()
#
#     return render(request, 'predict.html',
#                   {'form': form,'predicted': predicted,'user_id':u_id,'predictions':predictions})
