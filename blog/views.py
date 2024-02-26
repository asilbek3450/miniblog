from django.shortcuts import render, redirect, get_object_or_404

from blog.forms import BlogForm
from blog.models import BlogPost, BlogCategory


# Create your views here.
def blog_list(request):
    bloglar = BlogPost.objects.all()
    categories = BlogCategory.objects.all()
    context = {
        'blogs': bloglar,
        'categories': categories
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


def blog_detail(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    category = BlogCategory.objects.filter(id=blog.category.id)
    context = {
        'blog': blog,
        'category': category,
    }
    return render(request, 'blog_detail.html', context=context)
