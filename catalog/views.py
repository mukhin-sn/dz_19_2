from django.shortcuts import render


# Create your views here.

def my_controller_1(request):
    return render(request, 'catalog/index.html')


def my_controller_2(request):
    return render(request, 'catalog/index_2.html')
