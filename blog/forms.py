from django.forms import ModelForm

from blog.models import BlogPost, BlogCategory


class BlogForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'short_description', 'description', 'image', 'category', 'author']


class BlogCategoryForm(ModelForm):
    class Meta:
        model = BlogCategory
        fields = ['name']

