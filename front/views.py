from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    context = {}
    return render(request, 'front/default.html', context)