from django.http import HttpResponse
from django.shortcuts import render
import joblib

def premiumpredict(request):
    return render(request,'premiumpredict.html')


def predict(request):
    cls=joblib.load('final_model.sav')
    lis = []

    lis.append(request.GET['age'])
    lis.append(request.GET['sex'])
    lis.append(request.GET['bmi'])
    lis.append(request.GET['children'])
    lis.append(request.GET['smoker'])

    ans=cls.predict([lis])

    return render(request,'predict.html',{'ans':ans})
