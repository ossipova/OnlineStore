from django.shortcuts import render, redirect
from products.models import Product, Review
from products.forms import ProductCreateForm, ReviewCreateForm
from django.views.generic import ListView

# Create your views here.

PAGINATION_LIMIT = 3


class MainView(ListView):
    model = Product


class ProductsCBV(ListView):
    model = Product

    def get(self, request, **kwargs):
        products = self.get_queryset()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if search:
            products = self.model.objects.filter(
                description__icontains=search
            ) | self.model.objects.filter(
                title__icontains=search
            )

        """max page"""
        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        """slice posts by page"""
        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        context = {
            'products': products,
            'user': request.user,
            'max_page': range(1, max_page + 1)
        }
        return render(request, self.template_name, context=context)


def product_detail_view(request, product_id):
    if request.method == 'GET':
        product = Product.objects.get(id=product_id)
        reviews = Review.objects.filter(product_id=product_id)

        context = {
            'product': product,
            'reviews': reviews,
            'form': ReviewCreateForm,
            'user': request.user
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        reviews = Review.objects.filter(product_id=product_id)

        form = ReviewCreateForm(data=request.POST)
        if form.is_valid():
            Review.objects.create(
                author=request.user,
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
            return redirect('/products')
        return render(request, 'products/create.html', context={
            'form': form
        })
