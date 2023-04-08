from django.shortcuts import render
from teste.models import Pessoa

def home(request):
    return render(request,'index.html')

def calcular(request):
    if request.method == 'POST':
        n1 = float(request.POST.get('v1'))
        n2 = float(request.POST.get('v2'))
        op = request.POST.get('op')
        if op == '+':
            total = n1+n2
        elif op == '-':
            total = n1-n2
        elif op == '*':
            total = n1*n2 
        else:
            total = n1/n2   
        context = {'v1':n1,'v2':n2,'total':total}
    return render(request,'index.html',context)

    def mostrarBD(request):
       ...
