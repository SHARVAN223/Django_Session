from django.shortcuts import render, redirect
from .models import Employee

def landing(req):
    return render(req , 'landing.html')

def registration(req):
    n=req.POST.get('name')
    e=req.POST.get('email')
    c=req.POST.get('number')
    p=req.POST.get('password')
    q = req.POST.getlist('qualification')
    g= req.POST.get('gender')
    s= req.POST.get('state')
    print(n,e,c,p,q,g,s,sep=",")
    return render(req, 'Registration.html')
    # return render(req, 'Registration.html')

def login(req):
    return render(req,'login.html')
    
def set_session(req):
    if req.method == 'POST':
        n=req.POST.get('name')
        e=req.POST.get('email')
        c=req.POST.get('number')
        p=req.POST.get('password')
        q = req.POST.getlist('qualification')
        g= req.POST.get('gender')
        s= req.POST.get('state')
        req.session['name']=n
        req.session['email']=e
        req.session['number']=c
        req.session['password']=p
        req.session['qualification'] =q
        req.session['gender']=g
        req.session['state']=s
        return render(req, 'landing.html',{'msg':"set session sucessful"})
    return render(req, 'registration.html')


def get_session(req):
    print(req.session)
    n = req.session.get('name')
    e=req.session.get('email')
    c=req.session.get('number')
    p=req.session.get('password')
    q = req.session.get('qualification')
    g= req.session.get('gender')
    s= req.session.get('state')
    get= {'name':n, 'email':e, 'password':p, 'number':c,'qualification':q, 'gender':g , 'state':s,}
    return render(req, 'landing.html',{'data': get}) 
    


def delete_session (req):
    if 'name' in req.session :
        req.session.flush()
        return render(req, 'landing.html',{'msg1':'session deleted'})
    return render(req, 'landing.html')


def sqlite(req):
    n=req.POST.get('name')
    e=req.POST.get('email')
    c=req.POST.get('number')
    p = req.POST.get('password')
    q = req.POST.getlist('qualification')
    g= req.POST.get('gender')
    s= req.POST.get('state')

    Employee.objects.create(
        Name = n,
        Email = e, 
        Password = p,
        Contact = c,
        Qualification = q,
        Gender = g,
        State = s
    )
    return redirect('login')
