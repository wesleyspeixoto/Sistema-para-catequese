from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def cadastro(request):
    return render(request, "cadastro.html")
