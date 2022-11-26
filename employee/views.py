from django.http import HttpResponse


def api_login(request):
    if request.method == 'POST':
        return HttpResponse("qr")


def api_logout(request):
    return HttpResponse("logout")

