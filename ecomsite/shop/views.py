from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator


def index(request):
    product_objects = Products.objects.all()

    # search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    # paginator code
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects': product_objects})

def detail(request,id):
    product_object = Products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_object':product_object})