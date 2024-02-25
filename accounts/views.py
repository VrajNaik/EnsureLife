from django.shortcuts import render , redirect
from .models import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User, auth
# Create your views here.
def postRequest(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    contact_no = request.POST['contact_no']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    value = {
        'first_name' : first_name,
        'last_name' : last_name,
        'contact_no' : contact_no,
        'email' : email
    }
    err_msg = None
    if password == confirm_password:
        customer = Customer(first_name = first_name,
                            last_name = last_name,
                            contact_no = contact_no,
                            email = email,
                            password = password)
        err_msg = customer.validateCustomer()
    else:
        err_msg = "Password Did not match!"
    if not err_msg:
        customer.password = make_password(customer.password)
        customer.rgstr()
        return redirect('/')
    else:
        data = {
            'err' : err_msg,
            'values' : value
        }
        return render(request,'register.html',data)

def register(request):
    if request.method == 'POST':
        return postRequest(request)
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'form.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        err_msg = None
        if customer :
            flag = check_password(password , customer.password )
            if flag :
                request.session['email'] = customer.email;
                request.session['customer_id'] = customer.id;
                request.session['first_name'] = customer.first_name;
                request.session['last_name'] = customer.last_name;
                return render(request,'index.html',{'customer' : customer})
            else:
                err_msg = 'Email or Password Invalid !!'
        else:
            err_msg = 'Email or Password Invalid !!'
        print(customer)
        print(email,password)
        return render(request , 'form.html', {'err' : err_msg, 'customer' : customer})

def logout(request):
    request.session.flush()
    return redirect('/')

def edit_profile(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        contact_no = request.POST['contact_no']
        email = request.POST['your_email']
        customer_id = request.session.get('customer_id')
        customer = Customer.objects.get(id=customer_id)
        customer.first_name=first_name
        customer.last_name=last_name
        customer.contact_no=contact_no
        customer.email=email
        customer.save()
        email = request.session.get('email')
        first_name = request.session.get('first_name')
        return render(request,'index.html',{'save':True,'email' : email,'first_name':first_name})
    else:
        customer_id=request.session.get('customer_id')
        customer=Customer.objects.filter(id=customer_id)
        email = request.session.get('email')
        first_name = request.session.get('first_name')
        return render(request,"edit_profile.html",{'user': customer[0],'email' : email,'first_name':first_name})
def profile(request):
    customer_id=request.session.get('customer_id')
    customer_profile=Customer.objects.filter(id=customer_id)
    # print(customer_profile[0])
    email = request.session.get('email')
    first_name = request.session.get('first_name')
    return render(request,"your_profile.html",{'user': customer_profile[0],'email' : email,'first_name':first_name})