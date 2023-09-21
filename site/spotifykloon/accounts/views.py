from django.shortcuts import render
# Create your views here.

def login_page_view(request):
    if request.method == "GET":
        return render(request, template_name="login.html")
    else:
        raise NotImplementedError("CANT DO THAT YET SORRY OwO")