from django.urls import path
from .views import *

urlpatterns = [
    path('', indexViews.index,name="myadmin_index"),  #后台首页


    #用户管理
    path('user/index', userViews.userindex, name="myadmin_userindex"),
    path('user/add',userViews.useradd,name="myadmin_useradd"),
    path('user/delete',userViews.userdelete,name="myadmin_userdelete"),
    path('user/edit/<int:uid>',userViews.useredit,name="myadmin_useredit"),


    # 图书分类
    path('booktype/index',booktypeViews.typeindex,name="myadmin_booktypeindex"),
    path('booktype/add',booktypeViews.typeadd,name="myadmin_typeadd"),
    path('booktype/delete',booktypeViews.typedelete,name="myadmin_typedelete"),
    path('booktype/edit',booktypeViews.typeedit,name="myadmin_typeedit"),



    #图书页面
    path('books/index',booksViews.bookindex,name="myadmin_bookindex"),
    path('books/add',booksViews.bookadd,name="myadmin_bookadd"),
    path('books/delete',booksViews.bookdelete,name="myadmin_bookdelete"),
    path('books/edit/<int:bid>',booksViews.bookedit,name="myadmin_bookedit"),
    path('books/bing',booksViews.bookbing,name="myadmin_bookbing"),


]