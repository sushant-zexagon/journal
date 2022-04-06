from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from .models import Entry, User
# Create your views here.
def home(request):
	user = request.session.get('user')
	if user:
		entries = Entry.objects.filter(user = user)
		data = {"entries":entries}
		return render(request,'notes/home.html', context = data)
	else:
		return redirect('/login/')

class Signup(View):
	def get(self, request):
		return render(request, 'notes/signup.html')
	
	def post(self, request):
		data = request.POST
		error = ''
		if data:
			name = data.get('full')
			if not name.isalpha() or len(name) == 0:
				error = 'Improper Name!'
			dob = data.get('dob')
			email = data.get('email')
			if '@' not in email or '.' not in email or len(email) <= 2:
				error = 'Improper Email Id!'
			users = User.objects.filter(email = email)
			if len(users) > 0:
				error = 'Email already exists!'
			password = data.get('pwd')
			if len(password) < 8:
				error = 'Password should be longer'
			if len(error) == 0:
				print(name, dob, email, password)
				user = User(name=name, dob=dob, password=password, email=email)
				user.password = make_password(user.password)
				user.save()
				return redirect('/login/')
			else:
				return render(request, 'notes/signup.html',{'error':error})
		else:
			return render(request, 'notes/signup.html')	


class Login(View):
	def get(self, request):
		return render(request, 'notes/login.html')
	def post(self, request):
		print('post function called')
		data = request.POST
		error = ''
		if data:
			print('inside data true if')
			email = data.get('email')
			password = data.get('pwd')
			users = User.objects.filter(email = email)
			if len(users) == 0:
				error = 'User does not exist!'
			else:
				if not check_password(password, users[0].password):
					error = 'Password does not match!'
				else:
					print('password matched')
					request.session['user'] = users[0].id
					return redirect('/home/')
		else:
			error = 'Please provide the information!'
		return render (request,'notes/login.html',{'error':error})



def logout(request):
	request.session['user'] = None

