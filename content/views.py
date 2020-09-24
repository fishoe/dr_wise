from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
import requests
def first_page(request):
    
    qcont = {
        'question':med_q[0][0],
        'answer':med_q[0][1],
    }

    html_tag = render(request,'question.html',qcont).content
    content = {
        'html': html_tag.decode('utf-8'),
    }

    return render(request,'main.html',content)

def result_page(request):
    print('thatthat')
    if request.method == 'POST':#이 페이지는 post로만 입장 가능
        print('that',request.POST)
        url = 'http://apis.data.go.kr/B551182/hospInfoService/getHospBasisList?serviceKey=GUeG6aQvm%2F%2F8AE5zdrZzjfQ3ejC5G36vtHwAbkW4IDBUPAHLfvnnn%2Fs%2FLlcr5bzFTjcOZJpklFMo4s4bsgpu%2BA%3D%3D'
        page = '&pageNo=1'
        numrow = '&numOfRows=20'
        clCd = '&clCd=' + request.POST['clCd'] 
        sbjCd = '&dgsbjtCd=' + request.POST['dgsbjtCd']
        xPos= '&xPos=' + request.POST['pos'].split(',')[0]
        yPos= '&yPos=' + request.POST['pos'].split(',')[1]
        radius= '&radius = 5000'
        t = '&_type=json'

        totalurl = url + page + numrow + clCd + sbjCd + xPos + yPos + radius + t

        res = requests.get(totalurl)
        # print(res.content)
        # print(request.POST['pos'])
        # print(request.POST['pos'].split(','))
        lon = float(request.POST['pos'].split(',')[0])
        lat = float(request.POST['pos'].split(',')[1])
        content = {
            'pos_long': lon ,
            'pos_lat': lat
        }
        return render(request,'result.html',content)
    else :
        return render(request,'result.html')

def question(request):
    print('start')
    if request.method == 'POST':
        req_json = eval(request.body)
        print(req_json)
        qn = int(req_json['answer'])
        qcont = {
            'question':med_q[qn][0],
            'answer':med_q[qn][1],
        }
        html_tag = render(request,'question.html',qcont).content

        content = {
            'html': html_tag.decode('utf-8'),
        }
        return JsonResponse(content)


'''
1. 통증이 있나요?
1. 있음 2. 없음
2. (1-2선택)어떤 불편함이 있으신가요?
1. 정신적(정신과) 2. 심리적(심리상담) 3. 수면(정신과,신경과) 4. 기억력(신경과)
'''

'''
--------------------------------------------------------------------------------------

1. 통증이 있나요?
1. 있음 2. 없음
2. 어디가 아프신가요 ?
1.상체 2. 하체 3. 전신 4. 피부 5.기타
3. {2-1답변}의 어디가 아프신가요 ?
1.머리 2.목 3.가슴 4.배 5.등 6.팔 7.얼굴

4. {3-1답변}의 증상의 원인은 어디인가요 ?
1.신체 내부(신경과) 2.신체 외부(외과)

4. {3-2답변}의 증상의 원인은 어디인가요 ?
1.신체 내부(이비인후과) 2.신체 외부(외과)

4. {3-3답변}의 증상의 원인은 어디인가요 ?
1.신체 내부(종합병원) 2.신체 외부(외과)

4. {3-4답변}의 증상의 원인은 어디인가요 ?
1.신체 내부(내과) 2.신체 외부(외과)

4. {3-5답변}의 증상의 원인은 어디인가요 ?
1.신체 내부(신경외과) 2.신체 외부(외과)

4. {3-6답변}의 증상의 원인은 어디인가요 ?
1.신체 내부(신경외과) 2.신체 외부(정형외과)

4. {3-7답변}의 증상의 원인은 어디인가요 ?
1.신체 내부(신경외과) 2.눈(안과) 3. 코, 귀(이비인후과) 4. 그 외 외부(외과)
'''
med_q = [
    ['통증이 있나요?',[('있음','q1'),('없음','q2')]],#q0
    ['어디가 아프신가요',[('상체','q3'),('하체','q11'),('피부','a21_14')]],#q1
    ['어떤 불편함이 있으신가요?',[('정신적','a21_03'),('심리적','a21_03'),('수면','a21_02'),('기억력','a21_02')]],#q2
    ['어디가 아프신가요',[('머리','q4'),('목','q5'),('가슴','q6'),('배','q7'),('등','q8'),('팔','q9'),('얼굴','q10')]],#q3
    ['증상의 원인이 어디인가요?',[('신체 내부','a21_02'),('신체 외부','a21_04')]],#q4
    ['증상의 원인이 어디인가요?',[('신체 내부','a21_13'),('신체 외부','a21_04')]],#q5
    ['증상의 원인이 어디인가요?',[('신체 내부','a11_07'),('신체 외부','a21_04')]],#q6
    ['증상의 원인이 어디인가요?',[('신체 내부','a21_01'),('신체 외부','a21_04')]],#q7
    ['증상의 원인이 어디인가요?',[('신체 내부','a11_06'),('신체 외부','a21_04')]],#q8
    ['증상의 원인이 어디인가요?',[('신체 내부','a11_06'),('신체 외부','a21_05')]],#q9
    ['증상의 원인이 어디인가요?',[('신체 내부','a11_06'),('눈','a21_12'),('코,귀','a21_13'),('그 외 외부','a21_04')]],#q10
    ['어디가 아프신가요',[('생식기','a21_15'),('다리','q12')]],#q11
    ['증상의 원인이 어디인가요?',[('신체 내부','a11_06'),('신체 외부','a21_05')]],#q12
]
'''
--------------------------------------------------------------------------------------

1. 통증이 있나요?
1. 있음 2. 없음
2. (1-1선택)어디가 아프신가요 ?
1.상체 2. 하체 3. 피부
3. {2-2답변}의 어디가 아프신가요 ?
1. 생식기(비뇨기과) 2. 다리 

4. {3-2답변}의 증상의 원인은 어디인가요 ?
1.신체 내부(신경외과) 2.신체 외부(정형외과)
'''

'''
dgsbjtCd
00:일반의, 01:내과, 02:신경과, 03:정신건강의학과, 04:외과, 05:정형외과, 06:신경외과, 07:흉부외과,
12:안과, 13:이비인후과, 14:피부과, 15:비뇨기과,23:가정의학과
'''

'''
clcd
01:상급종합병원, 05:전문병원, 11:종합병원, 21:병원, 28:요양병원, 31:의원, 41:치과병원, 51:치과의원, 61:조산원, 71:보건소, 72:보건지소, 73:보건진료소, 75:보건의료원, 81:약국, 91:한방종합병원, 92:한방병원, 93:한의원
- 전문병원은 제외
'''

'''http://apis.data.go.kr/B551182/hospInfoService/getHospBasisList?serviceKey=GUeG6aQvm%2F%2F8AE5zdrZzjfQ3ejC5G36vtHwAbkW4IDBUPAHLfvnnn%2Fs%2FLlcr5bzFTjcOZJpklFMo4s4bsgpu%2BA%3D%3D
&pageNo=1
&numOfRows=10
&sidoCd=240000
&sgguCd=
&emdongNm=
&yadmNm=
&zipCd=2030
&clCd=
&dgsbjtCd=02
&xPos=
&yPos=
&radius=
&_type=json'''

'http://apis.data.go.kr/B551182/hospInfoService/getHospBasisList?serviceKey=GUeG6aQvm%2F%2F8AE5zdrZzjfQ3ejC5G36vtHwAbkW4IDBUPAHLfvnnn%2Fs%2FLlcr5bzFTjcOZJpklFMo4s4bsgpu%2BA%3D%3D&pageNo=1&numOfRows=100&sidoCd=240000&clCd=21&dgsbjtCd=04&_type=json'