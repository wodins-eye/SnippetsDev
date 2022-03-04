
from django.urls import path

from snippets import views

app_name = 'snippets'

urlpatterns = [
    path('', views.homeView, name= 'Home'),
    path('addSnippet/', views.addSnippetView, name= 'AddSnip'),
    path('editSnippet/<int:pk>/', views.editSnippetView.as_view(), name= 'EditSnip'),
    path('deleteSnippet/<int:pk>/', views.deleteSnippetView.as_view(), name= 'DelSnip'),
    path('addLanguage/', views.addLanguageView, name= 'AddLang'),
    path('addPackage/', views.addPackageView, name= 'AddPack'),
    path('addApplication/', views.addApplicationView, name= 'AddApp'),
    # These are JSON return used by JS to get lists of objects
    path('getlanguages/', views.getLanguages, name= 'GetLangs'),
    path('getpackages/', views.getPackages, name= 'GetPacks'),
    path('getapplications/', views.getApplications, name= 'GetApps'),
    # Load the filtered snippets
    path('languages/<str:lang>/', views.filterByLanguageView, name= 'LangView'),
    path('packages/<str:pack>/', views.filterByPackageView, name= 'PackView'),
    path('applications/<str:app>/', views.filterByApplicationView, name= 'AppView'),
    path('/snippetDetail/<int:pk>/', views.detailSnippetView.as_view(), name= 'Detail'),

]