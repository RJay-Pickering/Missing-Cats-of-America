from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm

from app.models import KittyCats
from .forms import CreateUserForm, CreateKatForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.

@unauthenticated_user
def userregisterPage(request):
	form=CreateUserForm()
	if request.method == "POST":
		form=CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, "Created " + username)
			group = Group.objects.get(name="customer")
			user.groups.add(group)
			return redirect('userlogin')
	context = {'form':form}
	return render(request, 'user_register.html',context)

@unauthenticated_user
def userloginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password = password)
		if user is not None:
			login(request, user)
			return redirect("home")
		else:
			messages.info(request, "Username or Password is incorrect")
	context = {}
	return render(request, 'user_login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('userlogin')

@login_required(login_url='userlogin')
@admin_only
@allowed_users(allowed_roles=['admin'])
def home(request):
	kats = KittyCats.objects.all()
	context = {"kats": kats}
	return render(request, "index.html", context)

@login_required(login_url='userlogin')
def userhome(request):
	kats = KittyCats.objects.all()
	return render(request, "user-page.html", {"kats": kats})

def contact(request):
	return render(request, "user-page.html")

@login_required(login_url='userlogin')
def create(request):
	form = CreateKatForm()
	if request.method == "POST":
		post = request.POST.copy() # to make it mutable
		post['user'] = request.user.username
		# and update original POST in the end
		request.POST = post
		form = CreateKatForm(request.POST, request.FILES)
		print(request.user.username)
		print(form.errors)
		if form.is_valid():
			form.save()
			return redirect("home")
	context = {"form": form,"time":"Create"}
	return render(request, "create.html", context)

@login_required(login_url='userlogin')
def update(request, pk):
	cat = KittyCats.objects.get(id=pk)
	form = CreateKatForm(instance=cat)
	if request.method == "POST":
		print(request.POST)
		form = CreateKatForm(request.POST, instance=cat)
		if form.is_valid():
			form.save()
			return redirect("home")

	context = {"form": form, "time":"Update"}
	return render(request, "create.html", context)

@login_required(login_url='userlogin')
def delete(request, pk):
	item = KittyCats.objects.get(id=pk)
	if request.method == "POST":
		item.delete()
		return redirect("home")
		
	context={"item": item}
	return render(request, "delete.html",context)