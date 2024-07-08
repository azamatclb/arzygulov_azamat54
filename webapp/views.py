from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.models import Product, Category
from webapp.validation import validation


def index(request):
    products = Product.objects.filter(in_stock=1)
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
        return redirect('products')
    else:
        category = Category()
    return render(request, 'new_category.html', context={'category': category})


def add_product(request):
    errors = {}
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        category_id = request.POST.get("category")
        price = request.POST.get("price")
        image = request.POST.get("image")
        in_stock = request.POST.get('in_stock')

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            category = None
            errors['category'] = "Category doesn't exist"

        product = Product(
            title=title,
            description=description,
            category_id=category_id,
            price=price,
            image=image,
            in_stock=in_stock
        )

        errors.update(validation(product))

        if not errors:
            product.save()
            return redirect('products')

    return render(request, 'new_product.html',
                  context={'categories': Category.objects.all(),
                           'product': Product(),
                           'errors': errors})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect('products')
    else:
        return render(request, 'delete_product.html', context={"product": product})


def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    errors = {}

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        category_id = request.POST.get("category")
        price = request.POST.get('price')
        image = request.POST.get('image')
        in_stock = request.POST.get('in_stock')

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            category = None
            errors['category'] = "Category doesn't exist"

        if category:
            product.title = title
            product.description = description
            product.category = category
            product.price = price
            product.image = image
            product.in_stock = in_stock

            errors = validation(product)

            if not errors:
                product.save()
                return redirect('product_view', pk=product.pk)

        return render(request, "update_product.html", {
            "product": product,
            'categories': Category.objects.all(),
            'errors': errors
        })

    return render(request, "update_product.html", {
        "product": product,
        'categories': Category.objects.all(),
        'errors': errors
    })
