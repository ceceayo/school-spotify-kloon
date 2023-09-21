from django.http import HttpResponse
import datetime
# Create your views here.

def login_page_view(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)