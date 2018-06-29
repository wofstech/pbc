from django.shortcuts import render, redirect
from . models import Post, Members
from django.views import generic
from blog.forms import  CommentForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MemberForm
from django.contrib import messages



def index(request):
    post = Post.objects.all()[:7]

    context = {
        'post': post,
    }
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['Your_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['gabrielabuka@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "blog/contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')


class PostListView(generic.ListView):
    model = Post
    paginate_by = 10

class PostDetailView(generic.DetailView):
    model = Post

def add_comment_to_post(request, pk):
    post = Post.objects.get(pk = pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})
    
list = []
def register(request):
    a = Members.objects.all().count() + 1
    b = 'PBC/M/024/'
    if a < 10:
       b = 'PBC/M/024/00' 
    if a > 9 and a < 100:
       b = 'PBC/M/024/0'
    if a > 99:
       b = 'PBC/M/024/'
    list.append(a)
    if request.method == 'POST':
        member_form = MemberForm(request.POST) 
        if member_form.is_valid(): 
                       
            mem = member_form.save(commit=False)
            mem.pbc_number = b + str(a)
            mem.save()
            return redirect('confirm', a)           
    
    else:        
        member_form = MemberForm()         

    return render(request, 'blog/register.html', {'member_form': member_form, 'a': a, 'b': b})

def confirm(request, pk):
    reg = Members.objects.get(pk = list[-1])   
    return render(request, 'blog/confirm.html', {'reg': reg})