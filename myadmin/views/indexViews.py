
from django.shortcuts import render

# Create your views here.
# 主要存放后台首页

# 后台首页
def index(request):

    return render(request,"myadmin/index.html")