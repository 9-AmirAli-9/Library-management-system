from django.shortcuts import render
from .utils import *
# Create your views here.

def accounting_home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if isUsernameValid(username):
            # Proceed with the valid username
            pass

    return render(request, 'accounting/home.html')