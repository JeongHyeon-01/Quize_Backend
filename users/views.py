from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse


# redirect test용 추후 지워질 내용
def hello(request):
    return HttpResponse(200)
