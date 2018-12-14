from django.shortcuts import render

# Create your views here.
def my_cv(request):
    return render(request,'index.html')