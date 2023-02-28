from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

#blog post
from .models import Post
from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView


from django.urls import reverse_lazy

from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages

from .forms import BlogPostForm, EditBlogPostForm, PrayerForm
# Create your views here.



def index(response):
    return render(response, 'main/index.html')

def about(response):
    return render(response, 'main/about.html')

def contact(response):
    return render(response, 'main/contact.html')

def prayer_success(response):
    return render(response, 'main/prayer_success.html')






#def blog(response):
    #return render(response, 'main/blog.html')


#def blog_single(response):
    #return render(response, 'main/blog-single.html')




    

def addBlogPost(request):
    
   
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid(): 
            post = form.save()
            messages.success(request, 'Your blog post has been created!')
            return HttpResponseRedirect('blog')
        
        
    else:
        form = BlogPostForm()
    
    return render(request, 'main/addBlogPost.html', {'form': form})



def prayer_post(request):

    if request.method == 'POST':
        # This is the prayer request form
       
       form = PrayerForm(request.POST)
       if form.is_valid():
        form.save()
        return render(request, 'main/prayer_success.html')
    else:
        form = PrayerForm()
        return render(request, 'main/prayer.html')

   


class blog(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "main/blog.html"


class blog_single(generic.DetailView):
    model = Post
    template_name = "main/blog-single.html"


class editBlogPost(UpdateView):
    model = Post
    form_class = EditBlogPostForm
    template_name = "main/editblog.html"



class deleteBlogPost(DeleteView):
    model = Post
    
    template_name = "main/deleteblog.html"
    success_url = reverse_lazy('blog')
    
