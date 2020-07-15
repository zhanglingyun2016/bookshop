from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# 前台首页
def index(request):

    return render(request,"myhome/index.html")
