from django.db import models

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Package(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        val = getattr(self, 'name', False)
        if val:
            setattr(self, 'name', val)
        super(Package, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('snippets:snippetsAddSnippet')

class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)
    packages = models.ManyToManyField(Package, related_name='language')

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        val = getattr(self, 'name', False)
        if val:
            setattr(self, 'name', val)
        super(Language, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Application(models.Model):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        val = getattr(self, 'name', False)
        if val:
            setattr(self, 'name', val)
        super(Application, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class CodeSnippet(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    package = models.ManyToManyField(Package, related_name='snippets')
    application = models.ForeignKey(Application, on_delete=models.CASCADE, null=True)
    summary = models.CharField(max_length=500)
    code = RichTextField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    class Meta:
        ordering = ['last_modified']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('snippets:Home')

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super(CodeSnippet, self).save(*args, **kwargs)