from django.shortcuts import render

posts = [
	{
		'author': 'Piotrek',
		'title': 'Post nr 1',
		'content': 'Zawartosc posta nr 1',
		'date_posted': '10 lipca 2021',
	},
	{
		'author': 'Jane Doe',
		'title': 'Post nr 2',
		'content': 'Zawartosc posta nr 2',
		'date_posted': '11 lipca 2021',
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})


