from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is my Django app for the Web Frameworks assignment.")

