from django.shortcuts import render

def home(request):
	return render(request, 'blog/home.html', {'title': 'Test'})

def apropos(request):
	return render(request, 'blog/apropos.html', {'title': 'A propos'})

def contact(request):
	return render(request, 'blog/contact.html', {'title': 'Contact'})

