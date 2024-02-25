from django.shortcuts import render
from .models import Insurance

# Create your views here.
def Insurance_info(request):
    team = Insurance.objects.all()
    email = request.session.get('email')
    first_name = request.session.get('first_name')
    return render(request,"insurance.html",{'team' : team ,'email' : email,'first_name' : first_name})
def policyinfo(request):
    policy_name = request.GET.get('name');
    print(policy_name)
    if(policy_name):
        policy = Insurance.get_policy_by_name(policy_name)
        return render(request,"policyinfo.html",{'policy' : policy})
    else:
        return render(request, "insurance.html")