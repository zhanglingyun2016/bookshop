
# 分页模块
from django.core.paginator import Paginator
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,reverse
from ..models import User


# Create your views here.

# 会员管理-列表
def userindex(request):
    data = User.objects.all()
    """----------进行条件查询-----------"""
    # 获取后台搜索框表单数据
    drop = request.GET.get("drop",None)
    sout = request.GET.get("sout",None)
    #如果下拉框为空值
    if drop == "用户编号":
        data = data.filter(id__contains=sout)
    elif drop == "用户姓名":
        data = data.filter(username__contains=sout)
    elif drop == "手机号码":
        data == data.filter(phone__contains=sout)
    elif drop == "用户性别":
        data == data.filter(sex__contains=sout)

    """----------进行分页操作-----------"""
    # 实例化分页数据
    p = Paginator(data,10)   #一页10条数据
    # 获取当前页，默认为第一页
    page_index = request.GET.get("page",1)
    # 根据页码获取数据
    data = p.page(page_index)

    context = {"userdata":data}
    return render(request,"myadmin/users/index.html",context)


# 会员管理-添加
def useradd(request):
    if request.method == "GET":
        return render(request, "myadmin/users/add.html")
    else:
        data = request.POST.dict()
        data.pop("csrfmiddlewaretoken")
        print(data)
        #对数据进行处理
        # pbkdf2_密码加密
        from django.contrib.auth.hashers import make_password,check_password
        data["password"] = make_password(data["password"])

        # 3.成功后跳转到图书显示页面
        try:
            user = User(**data)
            user.save()
            url = reverse("myadmin_userindex")
            return HttpResponse(f'<script>alert("添加成功");location.href="{url}"</script>')
        except:
            return '<script>alert("添加失败");history.go(-1)</script>'

        return HttpResponse("post")





# 会员管理用户删除
def userdelete(request):
    try:
        # 获取传入的id
        id = request.GET.get("id")
        obj = User.objects.get(id=id)
        # 执行删除操作
        obj.delete()
        return JsonResponse({"error":0,"msg":"删除成功"})
    except:
        return JsonResponse({"error":1,"msg":"删除失败"})

    return HttpResponse("会员管理-删除")


# 会员管理-修改
def useredit(request,uid):
    # 判断uid参数
    try:
        obj = User.objects.get(id=uid)
    except:
        return HttpResponse('<script>alert("参数错误");history.go(-1)</script>')

    if request.method == "GET":
        # 获取对象
        #加载编辑表单
        return render(request,"myadmin/users/update.html",{"userobj":obj})
    else:
        # 获取表单数据
        data = request.POST.dict()
        data.pop("csrfmiddlewaretoken")
        # 完成数据更新
        obj = User.objects.filter(id=uid).update(**data)
        # 进行跳转
        url = reverse("myadmin_userindex")
        return HttpResponse(f'<script>alert("修改成功");location.href="{url}"</script>')











