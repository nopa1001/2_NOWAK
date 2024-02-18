from django.urls import path
from .views import index, detail, checkout
app_name = "shop"

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', detail, name='detail'),
    path('checkout/', checkout, name='checkout'),
]