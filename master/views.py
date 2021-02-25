from master.models import ContactModel, SubscribeModel
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.utils import timezone

# Create your views here.
index = lambda request: render(request, 'index.html', {})
contact = lambda request: render(request, 'contact.html', {})

def contact_request(request):
    if request.method != 'POST':
        return HttpResponseBadRequest(f'Bad request: {request.method}')
    data = request.POST
    new_contact_model = ContactModel(fname = data['w3lName'], lname = data['w3lLName'], email = data['w3lSender'], phone_num = data['w3lPhone'], subject = data['w3lSubject'], message = data['w3lMessage'], send_on = timezone.now())
    new_contact_model.save()
    return redirect('/contact/')

def subscribe_request(request):
    if request.method != 'POST':
        return HttpResponseBadRequest(f'Bad request: {request.method}')
    data = request.POST
    new_subscribe_form = SubscribeModel(email=data['email'], regdate=timezone.now())
    new_subscribe_form.save()
    return redirect('/')