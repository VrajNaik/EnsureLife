from django.shortcuts import render
from .models import Policy
from django.http import HttpResponse
import joblib

# Create your views here.
def policycompare(request):
    team = Policy.objects.all()
    first_name = request.session.get('first_name')
    return render(request, 'polcomp.html',{'team' : team,'first_name' : first_name})

def premiumcalc(request):
    return render(request, 'premiumcalc.html')

def compare(request):
        plan1 = request.POST.get('plan1')
        plan2 = request.POST.get('plan2')
        first_name = request.session.get('first_name')
        print(plan1, plan2)
        if plan1 != plan2:
            policy1 = Policy.get_policy_by_name(plan1);
            policy2 = Policy.get_policy_by_name(plan2);
            return render(request, 'compare.html',{'policy1' : policy1,'policy2' : policy2,'first_name' : first_name})
        elif plan1 == "Select any plan" or plan2 == "Select any plan" :
            err_msg = "Please Enter Values for Polices"
            return render(request, 'polcomp.html',{'err' : err_msg,'first_name' : first_name})
        elif plan1 == plan2:
            err_msg = "Please Enter UNIQUE values for two Policy to Do comparison"
            return render(request, 'polcomp.html',{'err' : err_msg,'first_name' : first_name})

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
