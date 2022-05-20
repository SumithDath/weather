from django.shortcuts import render
import requests
import json
# Create your views here.
def index(request):
    if request.method=='POST':
        city=request.POST['city']
        r=requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=05541db09d3829e5172ff0675ebd8946')
        if(r.status_code==404):
            return render(request,'sample.html',{'flag':1,'t1':False})
        k=r.content
        s=json.loads(k)
        a=s['name']
        b=s['weather'][0]['main']
        c=s['weather'][0]['description']
        l1=s['coord']['lon']
        l2=s['coord']['lat']
        t=round(s['main']['temp']-273,2)  #converting to celsius
        h=s['main']['humidity']
        p=s['main']['pressure']
        w=int(s['wind']['speed']*3.6)
    else:
        a=False
        b=False
        t=False
        p=False
        h=False
        l1=False
        l2=False
        w=False
    
    d={'a1':a,'b1':b,'l11':l1,'l21':l2,'t1':t,'p1':p,'h1':h,'w1':w}
    return render(request,'sample.html',d)
