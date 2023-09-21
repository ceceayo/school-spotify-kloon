from django.shortcuts import render
# Create your views here.

def login_page_view(request):
    return render(request, template_name="login.html")