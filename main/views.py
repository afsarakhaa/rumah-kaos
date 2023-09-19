from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def show_main(request):
    products = Product.objects.all()
    jumlah_produk = products.count()
    context = {
        'name': 'Acme De La Vie Baby Face Donut',
        'price': 'Rp850.000,00',
        'description': 'Kaos Acme De La Vie adalah kaos yang biasa dipakai oleh Koko-Koko di PIK',
        'image_url' : 'https://cdn.istyle.im/images/product/web/37/09/76/00/0/000000760937_01_800.png',
        'products' : products,
        'jumlah_produk' : jumlah_produk,

    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")