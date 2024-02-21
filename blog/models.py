from django.utils.text import slugify
from django.db import models


# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=128, verbose_name='Kategoriya nomi')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug', blank=True)

    def save(self, *args, **kwargs):
        # Generate slug automatically from the name
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Blog kategoriya'
        verbose_name_plural = 'Blog kategoriyalar'


class BlogPost(models.Model):
    title = models.CharField(max_length=128, verbose_name='Maqola nomi')
    description = models.TextField(verbose_name='Maqola haqida')
    short_description = models.TextField(verbose_name='Maqola qisqacha haqida')
    image = models.ImageField(upload_to='blog_images/', verbose_name='Maqola rasmi')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, verbose_name='Maqola kategoriyasi')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug', blank=True)

    view_count = models.IntegerField(default=0, verbose_name='Ko\'rishlar soni')
    author = models.CharField(max_length=50, verbose_name='Muallif')

    def save(self, *args, **kwargs):
        # Generate slug automatically from the title
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog maqola'
        verbose_name_plural = 'Blog maqolalar'

