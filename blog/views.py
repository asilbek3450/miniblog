from django.shortcuts import render, redirect

from blog.forms import BlogForm


# Create your views here.
def blog_list(request):
    return render(request, 'blog_list.html')


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
