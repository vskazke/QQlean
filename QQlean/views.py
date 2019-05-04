from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from QQlean.models import CallBack, Short
from .forms import CallBackForm, ShortForm



def indexlandingpage(request):
    return render(request, 'index-landingpage.html')


def index(request):
    form = CallBackForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_form = form.save()
        phone = request.POST['phone']
        summ_room = request.POST['summ_room']
        summ_bath = request.POST['summ_bath']
        
        q = CallBack(phone=phone, summ_room=summ_room, summ_bath=summ_bath)
        q.save()
        print(q)
        if phone:
            try:
                send_mail(phone, "phone: %s" % (phone),
                          settings.EMAIL_HOST_USER, ['zlatochka1972@bk.ru'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/')
        else:
            print('No')
            return HttpResponse('Make sure all fields are entered and valid.')
    shortform = ShortForm(request.POST or None)
    if request.method == "POST" and shortform.is_valid():
        new = shortform.save()
        phonesh = request.POST['phone']
            
        if phonesh:
            try:
                send_mail(phonesh, "phone: %s" % (phonesh),
                          settings.EMAIL_HOST_USER, ['zlatochka1972@bk.ru'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/')
        else:
            print('No')
            return HttpResponse('Make sure all fields are entered and valid.')

    return render(request, 'index.html', locals())



