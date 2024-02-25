from django.shortcuts import render
from .models import Devlopment_team

# Create your views here.
def about(request):
    team = Devlopment_team.objects.all()
    email = request.session.get('email')
    first_name = request.session.get('first_name')
    return render(request,"about.html",{'team' : team , 'email' : email,'first_name' : first_name})
def faq(request):
    email = request.session.get('email')
    first_name = request.session.get('first_name')
    return render(request, 'faq.html',{'email' : email,'first_name' : first_name})