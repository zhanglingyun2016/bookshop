from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,reverse
from ..models import Booktype


# 图书分类视图

# 图书列表显示
def typeindex(request):
    data = Booktype.objects.all()
    textparam = {"types": data}

    return render(request,"myadmin/booktype/index.html",textparam)




# 图书添加
def typeadd(request):
    if request.method == "GET":
        return render(request,"myadmin/booktype/add.html")
    else:
        data = request.POST.dict()
        data.pop("csrfmiddlewaretoken")
        print(data)

        # 是顶级分类
        if data["pid"] == 0:
            data["path"] = "0,"
        elif data["pid"] == 1:
            data["path"] = "0,2"

        # 进行添加
        try:
            obj = Booktype(**data)
            obj.save()
            url = reverse("myadmin_booktypeindex")
            return HttpResponse(f'<script>alert("添加成功");location.href="{url}"</script>')
        except:
            return HttpResponse('<script>alert("添加失败");history.go(-1)</script>')

        return HttpResponse("图书分类添加操作")



# 图书删除
def typedelete(request):
    try:
        id = request.GET.get("id")
        obj = Booktype.objects.get(id=id)
        obj.delete()

        return JsonResponse({"error": 0, "msg": "删除成功"})
    except:
        return JsonResponse({"error": 1, "msg": "删除失败"})

    return HttpResponse("图书分类列表-图书删除")



# 图书编辑
def typeedit(request):
    # try:
    data = request.POST.dict()
    obj = Booktype.objects.get(id=data["id"])
    obj.name = data["name"]
    obj.save()
    return JsonResponse({"error":0,"msg":"更新成功！"})
    # except:
    #     return JsonResponse({"error":1,"msg":"更新失败！"})





