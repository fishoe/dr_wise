from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse

def first_page(request):
    body_part = ['head','neck','shoulder','arms','chest','belly','back','hip','legs','others']
    body_part_kr = ['머리','목','어깨','팔','가슴','배','등','엉덩이','다리','그 외']

    if request.method == 'POST':
        req_json = eval(request.body)



        content = {
            'html':render(request,'sample.html',qestion).content
        }

        return JsonResponse(content)
    else : #GET    
        content = {
            'parts':zip(body_part,body_part_kr),
            'symptoms':{},
            'codes':'<input type="text" value="hello">',
        }
        sampledict={
            'head':'friend',
            'li':['first','second','third']
        }

        return render(request,'main.html',content)

def result_page(request):
    if request.method == 'POST':#이 페이지는 post로만 입장 가능
        content = {}
        return render(request,'result.html',content)
    else :
        return render(request,'result.html')

def question(request):
    print('start')
    if request.method == 'POST':
        req_json = eval(request.body)
        question = {
            'question':'새로운 질문들',
            'answer':[1,2,3,4,5]
        }
        html_tag = render(request,'question.html',question).content


        content = {
            'html': html_tag.decode('utf-8'),
        }
        print(content)
        return JsonResponse(content)