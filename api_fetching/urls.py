"""api_fetching URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fetch_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fetch/', views.fetchapi, name='fetchapi'),
    path('country/<str:code>', views.fetchcountry, name='fetchcountry')
]

# def fetchapi(request):
#     API_KEY ='7549e5fd4e214322b6bc2cbfe0c00ca6'
#     response = rq.get('https://newsapi.org/v2/top-headlines?country=us&apiKey='+API_KEY+'').json()
#     print(response['articles'])
#     return render(request, 'fetch.html', {'response': response})