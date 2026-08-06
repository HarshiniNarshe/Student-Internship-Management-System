from django.shortcuts import render
from django.http import HttpResponse
def he(request):
	return HttpResponse("<h1>Hello Harshini</h1>")
def data(request,b):
	return HttpResponse("<h2><center>My Name is :{}</center></h2>".format(b))
def temp(request):
	return render(request,'temp.html',{})
def table(request):
	return render(request,'table.html',{})


def details(request,id,name):
	return render(request,'details.html',{'i':789,'n':name})

def inline(request):
	return render(request,'inline.html')

def internal(request):
	return render(request,'internal.html')

def external(request):
	if request.method=="POST":
		na=request.POST['uname']
		mb=request.POST['mbl']
		e=request.POST['em']
		ps=request.POST['pwd']
		cps=request.POST['cpwd']
		return render(request,'data.html',{'n':na,'m':mb,'e':e,'p':ps,'cp':cps})
	return render(request,'external.html')
def boot(request):
	return render(request,'boot.html')

def offline(request):
	return render(request,'offline.html')