from django.shortcuts import render


# Create your views here.

def my_controller_1(request):
    return render(request, 'catalog/home.html')


def my_controller_2(request):
    context = {"data": False}

    if request.method == "POST":
        context["name"] = request.POST.get("name")
        context["phone"] = request.POST.get("phone")
        context["message"] = request.POST.get("message")
        context["data"] = True

        print(f'{context["name"]}, {context["phone"]}\n{context["message"]}')

    return render(request, 'catalog/contacts.html', context=context)
