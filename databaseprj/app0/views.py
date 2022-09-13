from django.shortcuts import render, redirect
from app0.models import Books_model
from app0.forms import Bookform
from django.contrib.auth.decorators import login_required
# Create your views here.
def home_view(request):
	return render(request,'app0/home.html')

def book_from(request):
	bkf = Bookform()
	if request.method=="POST":
		form = Bookform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/bkdata')
	return render(request,'app0/bkform.html',{"form":bkf})

@login_required
def book_data(request):
	bdt=Books_model.objects.all()
	return render(request,'app0/bkdata.html',{"bdata":bdt})

def student_view(request):
	bdt=Books_model.objects.all()
	return render(request,'app0/student.html',{"bdata":bdt})

def book_delete(request,id):
	bdel=Books_model.objects.get(id=id)
	bdel.delete()
	return redirect('/bkdata')

def book_update(request,id):
	bupd = Books_model.objects.get(id=id)
	if request.method=="POST":
		form=Bookform(request.POST,instance=bupd)
		if form.is_valid():
			form.save()
			return redirect('/bkdata')
	return render(request,'app0/bkupdate.html',{"bup":bupd})

def logout(request):
	return render(request,'app0/logout.html')

