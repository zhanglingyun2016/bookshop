from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]

# v1 /
# ├── db.sqlite3  # Django框架默认使用数据库文件
# ├── helloworld  # 创建的自定义应用
# │   ├── __init__.py
# │   ├── admin.py  # django框架自带后台模块配置文件
# │   ├── apps.py
# │   ├── migrations
# │   │   └── __init__.py
# │   ├── models.py  # 模型文件
# │   ├── tests.py  # 测试文件
# │   └── views.py  # 视图函数文件
# ├── manage.py  # 项目管理文件  所以的项目指令都需要manage.py
# └── v1  # 和项目同名的目录/ 存放于项目相关的配置文件 等
# ├── __init__.py  # 包初始化文件
# ├── settings.py  # 项目的配置文件
# ├── urls.py  # 项目的根路由文件
# └── wsgi.py  # 通用网关接口服务文件/后期上线部署到专业的HTTP服务器时需要用到