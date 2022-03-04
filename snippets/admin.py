from django.contrib import admin
from snippets.models import CodeSnippet, Language, Package
# Register your models here.

admin.site.register(CodeSnippet)
admin.site.register(Language)
admin.site.register(Package)