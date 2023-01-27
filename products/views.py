from django.shortcuts import render, redirect
from products.models import Product, Review
from products.forms import ProductCreateForm, ReviewCreateForm


# Create your views here.

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {'products': products

                   }
        return render(request, 'products/products.html', context=context)


def product_detail_view(request, product_id):
    if request.method == 'GET':
        product = Product.objects.get(id=product_id)
        reviews = Review.objects.filter(product_id=product_id)

        context = {
            'product': product,
            'reviews': reviews,
            'form': ReviewCreateForm
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        reviews = Review.objects.filter(product_id=product_id)

        form = ReviewCreateForm(data=request.POST)
        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                product=product
            )
            return redirect(f'/products/{product.id}')
        return render(request, 'products/create.html', context={
            'product': product,
            'reviews': reviews,
            'form': form
        })


def create_product_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)

        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
                currency=form.cleaned_data.get('currency'),
                rate=form.cleaned_data.get('rate'),
                commentable=form.cleaned_data.get('commentable')
            )
            return redirect ('/products')
        return render(request, 'products/create.html', context={
            'form': form
        })
