from django.shortcuts import render
from django.http import*
from app1.models import*
import re
import pandas as pd
from datetime import datetime
def list1(req):
    x=reg.objects.all()
    list1=x.values()
    print(x.values()[0])
    return render(req,"list.html",{"list1":list1})


def regi(req):
    return render(req,"reg.html")

def register(req):
    Name=req.POST.get('uname')
    if(checklength(Name)):
        Email=req.POST.get('uemail')
        if(checkmail(Email)):
            Pass=req.POST.get('upas')
            Phone=req.POST.get('uphone')
            Loc=req.POST.get('uloc')
            x=reg(sname=Name,semail=Email,spas=Pass,sphone=Phone,sloc=Loc)
            x.save()
            x=reg.objects.all()
            list1=x.values()
            print(x.values())
            s1="hello"+"  "+Name+" i know you password is "+Pass
        else:
            return render(req,'reg.html',{'error':'email shoul be in formate'})
        return render(req,"login.html",{"value":s1})
    else:
        return render(req,'reg.html',{'error':'username should be with in 5-10'})


def log(req):
    uname=req.POST.get('name')
    PWD=req.POST.get('pwd')
    ulist=reg.objects.all().values()
    uname_list=[]
    for i in ulist:
        uname_list.append(i['sname'])
    if(uname in uname_list):
        password=reg.objects.get(sname=uname)
        if(password.spas==PWD):
            x=reg.objects.all()
            req.session['id']=uname
            list1=x.values()
            return render(req,"dash.html")
        else:
            return HttpResponse("Password is worng")
    else:
            return render(req,"reg.html")


def login(req):
	return render(req,'login.html')

def checklength(sname):
    if len(sname)in range(5,11):
        return True
    else:
        return False
    
def checkmail(semail):
    a="^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
    if(re.search(a,semail)):
        return True
    else:
        return False

def menu(req):
    return render(req,'menu.html')

def logout(req):
    del req.session['id']
    return render(req,'login.html')
    '''
    try:
    	render(req,'login.html')
    except KeyError:
    	render(req,'login.html')
'''

def loc11(req):
	return render(req,"demo.html")
	
def new(req):
	x = reg.objects.get(sname=req.session['id'])
	print("--"*20)
	print(x.sname)
	print("--"*20)
	return render(req,"new.html",{"uname":x})

def main(req):
    return render(req,'main.html')

def sendmail(req):
    return render(req,'Mail.html')

def smtp_sendmail(email,subject,body,file):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("karthiks7520@gmail.com","hkdjkldoqehkrvow")

    message=f"subject:{subject}\n\n{body}\n\n{file}"
    server.sendmail("karthiks7520@gmail.com",email,message)
    server.quit()
    print("mail sent")

def submit(req):
    email=req.POST.get('email')
    subject=req.POST.get('subject')
    body=req.POST.get('body')
    file=req.POST.get('file')
    status="Pending..."
    loc=req.POST.get('Loc')
    curr_datetime = datetime.now().strftime('%d-%m-%y')
    curr_datetime1 = datetime.now().strftime('%H:%M:%S')
    y=pho4(photo=file,date1=curr_datetime,Time1=curr_datetime1,des=body,Status=status,Location=loc)
    y.save()
    smtp_sendmail(email,subject,body,file)
    return HttpResponse("mail sent")

def csv1(req):
    return render(req,"csv1.html")

def csv2(req):
    url=req.POST.get('csvurl')
    df=pd.read_csv(url)
    states=df['State'].unique()
    avg=df['Literacy'].mean()
    return render(req,"csv2.html",{'states':states,'avg':avg})

def issue(req):
    x=pho4.objects.all()
    file1=x.values()
    print(x.values())
    return render(req,"file1.html",{"file1":file1})


def demoo(req):
    a= req.POST.get('gps')
    print(a)
    x=loc(lang=a)
    x.save()
    return render(req,"menu.html")
