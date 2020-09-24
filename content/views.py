from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first_page(request):
    
    return HttpResponse('hi, world!')

def result_page(request):
    if request.method == 'POST':#이 페이지는 post로만 입장 가능
        content = {}
        return render(request,'result.html',context=content)
    else :
        return HttpResponse('wrong page req')