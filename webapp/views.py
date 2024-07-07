from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.models import Product, Category


def index(request):
    products = Product.objects.order_by("date_added")
    return render(request, 'index.html', context={"products": products})


def product_view(request, pk, *args, **kwargs):
    try:
        product = Product.objects.get(id=pk)
        pass
    except Product.DoesNotExist:
        return HttpResponseRedirect('/')
    return render(request, 'product_detail.html', context={'product': product})


def add_category(request):
    if request.method == "POST":
        Category.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description")
        )
        return HttpResponseRedirect(reverse('products'))
    else:
        category = Category()
    return render(request, 'new_category.html', context={'category': category})


def add_product(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        category_id = request.POST.get("category")
        price = request.POST.get("price")
        image = request.POST.get("image")
        in_stock = request.POST.get('in_stock')

        category = Category.objects.get(id=category_id)

        Product.objects.create(
            title=title,
            description=description,
            category=category,
            price=price,
            image=image,
            in_stock=in_stock
        )

        return HttpResponseRedirect(reverse('products'))

    return render(request, 'new_product.html', {'categories': Category.objects.all()})
