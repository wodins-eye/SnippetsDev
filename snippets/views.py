from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.core import serializers
from django.contrib.auth import decorators, mixins
from snippets.models import CodeSnippet, Language, Package, Application
from snippets import forms as fms


DEBUG = True

# Create your views here.
def homeView(request):

    recent_snippets = CodeSnippet.objects.order_by('last_modified')[:10:-1]

    context = {'recent_snippets': recent_snippets}

    return render(request, 'snippetsHome.html', context)

def filterByLanguageView(request, lang):
    snippets = CodeSnippet.objects.filter(language__name__contains=lang)


    context = {'recent_snippets': snippets}

    return render(request, 'snippetsFiltered.html', context)

def filterByPackageView(request, pack):
    snippets = CodeSnippet.objects.filter(package__name=pack)


    context = {'recent_snippets': snippets}

    return render(request, 'snippetsFiltered.html', context)

def filterByApplicationView(request, app):
    snippets = CodeSnippet.objects.filter(application__name=app)

    context = {'recent_snippets': snippets}

    return render(request, 'snippetsFiltered.html', context)

def getLanguages(request):
    """Get unique languages in Model Language and return JSON """

    lang_json = serializers.serialize('json', Language.objects.all())
    print(f'\nLANGS: {lang_json}')
    return JsonResponse(lang_json, safe=False, content_type='application/json')

def getPackages(request):
    """Get unique packages in Model Package and return JSON """

    pack_json = serializers.serialize('json', Package.objects.all())
    print(f'\nPACKS: {pack_json}')
    return JsonResponse(pack_json, safe=False, content_type='application/json')

def getApplications(request):
    """Get unique packages in Model Package and return JSON """

    app_json = serializers.serialize('json', Application.objects.all())
    print(f'\nPACKS: {app_json}')
    return JsonResponse(app_json, safe=False, content_type='application/json')

def addSnippetView(request):
    form = fms.snippetsEditForm()

    if request.method == 'POST':
        form = fms.snippetsForm(request.POST)
        print(f'\nFORM: {form.errors}')
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('snippets:Home'))

    context = {'form': form}

    return render(request, 'snippetAddSnippet.html', context)

class detailSnippetView(DetailView):
    model = CodeSnippet
    template_name = 'snippetsDetail.html'


class editSnippetView(mixins.UserPassesTestMixin, UpdateView):
    model = CodeSnippet
    form_class = fms.snippetsEditForm
    template_name = 'snippetsEditSnippet.html'

    def test_func(self):
        try:
            test = self.request.user.username == 'wodin'
        except AttributeError:
            test = False

        return test

class deleteSnippetView(mixins.UserPassesTestMixin, DeleteView):
    model = CodeSnippet
    template_name = 'snippetsDeleteSnippet.html'
    success_url = reverse_lazy('snippets:Home')

    def test_func(self):
        try:
            test = self.request.user.username == 'wodin'
        except AttributeError:
            test = False

        return test

def addPackageView(request):
    form = fms.snippetsAddPackageForm()

    if request.method == 'POST':
        form = fms.snippetsAddPackageForm(request.POST)
        if form.is_valid():

            form.save()
        return HttpResponseRedirect(reverse('snippets:AddSnip'))

    context = {'form': form, 'model': 'Package'}

    return render(request, 'snippetsAddEntry.html', context)

def addLanguageView(request):
    form = fms.snippetsAddLanguageForm()

    if request.method == 'POST':
        form = fms.snippetsAddLanguageForm(request.POST)
        if form.is_valid():

            form.save()
        return HttpResponseRedirect(reverse('snippets:AddSnip'))

    context = {'form': form, 'model': 'Language'}

    return render(request, 'snippetsAddEntry.html', context)

def addApplicationView(request):
    form = fms.snippetsAddApplicationForm()

    if request.method == 'POST':
        form = fms.snippetsAddApplicationForm(request.POST)
        if form.is_valid():

            form.save()
        return HttpResponseRedirect(reverse('snippets:AddSnip'))

    context = {'form': form, 'model': 'Application'}

    return render(request, 'snippetsAddEntry.html', context)