from django.urls import path
from .views import index, detail
from django.contrib import admin
app_name = "shop"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('<int:id>/', detail, name='detail')
]