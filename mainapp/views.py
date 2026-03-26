from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def fakultet(request):
    return render(request,'fakultet.html')
def kafedra(request):
    return render(request,'kafedra.html')
def fanlar(request):
    return render(request,'fanlar.html')
def ustozlar(request):
    return render(request,'ustozlar.html')
def talabalar(request):
    return render(request,'talabalar.html')