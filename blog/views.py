from django.shortcuts import render, redirect

from blog.forms import BlogForm
from blog.models import BlogPost


# Create your views here.
def blog_list(request):
    bloglar = BlogPost.objects.all()

    context = {
        'blogs': bloglar
    }
    # https://www.bootdey.com/snippets/view/Latest-News-section
    return render(request, 'blog_list.html', context=context)


def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')

        else:
            print('form is not valid', form.errors)
    else:
        form = BlogForm()
    context = {
        'form': form
    }

    return render(request, 'blog_create.html', context=context)


def blog_detail():
    pass
# https://www.bootdey.com/snippets/view/project-details