from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from QQlean.models import CallBack, Short
from .forms import CallBackForm, ShortForm



def indexlandingpage(request):
    return render(request, 'index-landingpage.html')


def index(request):
    #shortForm = ShortForm(request.POST or None)
    #if request.method == "POST" and shortForm.is_valid(
    #    new_form = shortForm.save()
    #    print(shortForm.cleaned_data)
    form = CallBackForm(request.POST or None)
    #  form_captcha = DemoForm(request.POST or None)
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
                          settings.EMAIL_HOST_USER, ['aleksauto.info@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse('sucsess')
        else:
            print('No')
            return HttpResponse('Make sure all fields are entered and valid.')

    return render(request, 'index.html', locals())


@csrf_exempt
def result(request):
    phone = request.POST['phone']
    summ_room = request.POST['summ_room']
    summ_bath = request.POST['summ_bath']
    
    q = CallBack(phone=phone, summ_room=summ_room, summ_bath=sum_bath)
    q.save()
    prin('llll')
    if phone:
        try:
            send_mail(phone, "phone: %s" % (phone),
                      settings.EMAIL_HOST_USER, ['aleksauto.info@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse('sucsess')
    else:
        print('No')
        return HttpResponse('Make sure all fields are entered and valid.')




