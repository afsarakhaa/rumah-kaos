from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name': 'Kaos Bayi Acme De La Vie',
        'amount': '100',
        'description': 'Kaos Acme De La Vie adalah kaos yang biasa dipakai oleh Koko-Koko di PIK'
    }

    return render(request, "main.html", context)