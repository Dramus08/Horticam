from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request,"index.html")

def allTransactionCash(request):

    return render(request,"allTransactionCash.html")