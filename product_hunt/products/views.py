from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.utils import timezone


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product_detail = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product_detail': product_detail})

@login_required
def publish(request):
    if request.method == 'GET':
        return render(request, 'publish.html')
    elif request.method == 'POST':
        app_name = request.POST['app_name']
        description = request.POST['description']
        app_link = request.POST['app_link']

        try:
            app_icon = request.FILES['app_icon']
            screen_shot = request.FILES['app_screen_shot']

            product = Product()
            product.app_name = app_name
            product.description = description
            product.app_link = app_link
            product.app_icon = app_icon
            product.screen_shot = screen_shot

            product.publish_date = timezone.datetime.now()
            product.hunter = request.user

            product.save()

            return redirect('home')
        except Exception as err:
            return render(request, 'publish.html', {'image_error': 'Please upload images.'})
