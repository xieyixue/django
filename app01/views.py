from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from app01 import models
from django.utils import timezone
# Create your views here.

def hello(request):
    print(request)
    ip = request.environ.get("REMOTE_ADDR",None)

    count = models.WebUser.objects.filter(ip=ip).count()

    if count == 0:
        models.WebUser.objects.create(ip=ip)
    else:
        web_user = models.WebUser.objects.filter(ip=ip).get()
        pv = web_user.pv + 1
        models.WebUser.objects.filter(ip=ip).update(pv=pv, update_time=timezone.now())

    data = models.WebUser.objects.filter(ip=ip).get()
    return render_to_response("hello.html",{"data": data})

