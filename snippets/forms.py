
from django import forms
from django.db.utils import OperationalError
from snippets.models import CodeSnippet, Package, Language, Application


class snippetsForm(forms.ModelForm):

    class Meta:

        model = CodeSnippet
        fields = ('name', 'author', 'language', 'package', 'application',
                  'summary', 'code')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control-small',}),
            'author': forms.TextInput(attrs={'value': '', 'id': 'writer', 'type': 'hidden'}),
            'language': forms.Select(choices=Language.objects.all().values_list('name', flat=True)),
            'package': forms.SelectMultiple(choices=Package.objects.all().values_list('name', flat=True)),
            'application': forms.Select(choices=Application.objects.all().values_list('name', flat=True)),
            'summary': forms.Textarea(attrs={'class': 'form-control',}),
            'code': forms.Textarea(attrs={'class': 'form-control',}),
        }

class snippetsEditForm(forms.ModelForm):

    class Meta:

        model = CodeSnippet
        fields = ('name', 'language', 'package', 'application',
                  'summary', 'code')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control-small', }),
            'language': forms.Select(choices=Language.objects.all().values_list('name', flat=True)),
            'package': forms.SelectMultiple(choices=Package.objects.all().values_list('name', flat=True)),
            'application': forms.Select(choices=Application.objects.all().values_list('name', flat=True)),
            'summary': forms.Textarea(attrs={'class': 'form-control', }),
            'code': forms.Textarea(attrs={'class': 'form-control', }),
        }
#
class snippetsAddLanguageForm(forms.ModelForm):

    class Meta:

        model = Language
        fields = ('name', )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control-small',
                                           }),
        }

class snippetsAddPackageForm(forms.ModelForm):

    class Meta:
        model = Package
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control-small',
                                           }),
        }

class snippetsAddApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control-small',
                                           }),
        }