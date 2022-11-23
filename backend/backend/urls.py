"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from backend import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from django.conf import settings

# Django Defaults
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index)
]

# API
urlpatterns += format_suffix_patterns([
    path('api/fibonacci/', views.fibonacci_list, name="fibonacci"),
    path('api/fibonacci/<int:id>', views.fibonacci_detail, name="fibonacci-details"),
])

# Loading Static Fiels
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)