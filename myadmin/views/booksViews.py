
# 分页模块
from django.core.paginator import Paginator
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,reverse
from ..models import Booktype,Books


# 图书页面
def bookindex(request):
    data = Books.objects.all()
    taxtparm = {"books":data}

    return render(request,"myadmin/books/index.html",taxtparm)


# 图书添加页面
def bookadd(request):
    if request.method == "GET":
        return render(request,"myadmin/books/add.html")
    else:
        try:
            data = request.POST.dict()
            data.pop("csrfmiddlewaretoken")
            print(data)
            obj = Books(**data)
            obj.save()
            url = reverse("myadmin_bookindex")
            return HttpResponse(f'<script>alert("添加成功");location.href="{url}"</script>')
        except:
            return HttpResponse(f'<script>alert("添加失败");history.go(-1)</script>')

    return render(request,"myadmin/books/add.html")



# 删除
def bookdelete(request):
    try:
        id = request.GET.get("id")
        obj = Books.objects.get(id=id)
        obj.delete()
        return JsonResponse({"error":0,"msg":"删除成功！"})
    except:
        return JsonResponse({"error":1,"msg":"删除失败!"})

    return HttpResponse("图书bookdelete")



# 编辑
def bookedit(request,bid):
    # 判断请求
    obj = Books.objects.get(id=bid)
    if request.method == "GET":
        textparam = {"obj":obj}
        return render(request,"myadmin/books/update.html",textparam)

    else:
        data = request.POST.dict()
        data.pop("csrfmiddlewaretoken")
        print(data)
        obj = Books.objects.filter(id=bid).update(**data)
        url = reverse("myadmin_bookindex")
        return HttpResponse(f'<script>alert("修改成功");location.href="{url}"</script>')

    return HttpResponse("图书bookedit")




def bookbing(request):
    book1 = Books.objects.get(id=2)
    book2 = Books.objects.get(id=4)
    book3 = Books.objects.get(id=5)
    book4 = Books.objects.get(id=6)
    book5 = Books.objects.get(id=7)
    print("张凌云。。。。。。。。。。。。。。。。。")
    textparam = {"obj1":book1,"obj2":book2,"obj3":book3,"obj4":book4,"obj5":book5}

    return render(request,"myadmin/books/bing.html",textparam)






