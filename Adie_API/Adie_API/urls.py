"""Adie_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from api.resources import AdieResource
from api.resources import CompanyResource
from api.resources import OfferResource
from api.views import hello_world


adie_resource = AdieResource()
company_resource = CompanyResource()
offer_resource = OfferResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(adie_resource.urls)),
    url(r'^api/', include(company_resource.urls)),
    url(r'^api/', include(offer_resource.urls)),
]




# urlpatterns = [
#     path('admin/', admin.site.urls),
#     url(r'^$', hello_world, name='adieapi_hello_world'),
# ]
