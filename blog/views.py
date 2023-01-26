from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    return render(request, "home.html")

def posts(request):
    posts = reversed(Post.objects.all())
    context = {"posts" : posts,}
    return render(request, "posts.html", context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        msg = "Thank you " + name + " for your feedback, your response has been recorded."
        return render(request, "contact.html", {"msg": msg})
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def postinfo(request, title):
    post = Post.objects.get(title=title)
    context = {"post": post}
    return render(request, "postinfo.html", context)