from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum
from .models import payment
from django.shortcuts import render, redirect

MERCHANT_KEY = '6olzLjOACe6Uss89'

def appoinment(request):
    id = request.POST.get('id')
    pay = request.POST.get('Payment')
    if request.method == 'POST':
        param_dict = {
            'MID': 'fxGUDc54100232327731',
            'ORDER_ID': id,
            'TXN_AMOUNT': pay,
            'CUST_ID': 'abc@gmail.com',
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/payment/handlerequest/',
        }
        email = request.session.get('email')
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'paytm.html', {'param_dict': param_dict})
    else:
        id=request.session.get('customer_id')
        email = request.session.get('email')
        first_name = request.session.get('first_name')
        customer = payment.objects.all()
        return render(request, 'policypayment.html',{'customer':customer,'first_name':first_name,'email':email})

@csrf_exempt
def handlerequest(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
            return render(request, 'paymentstatus.html', {'response': response_dict})
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
            return render(request, 'paymentstatus.html', {'response': response_dict})