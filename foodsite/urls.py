"""foodsite URL Configuration

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
from django.urls import path, include
from foodapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.cuisine_show, name='home'),
    path('admin/', admin.site.urls),
    path('cuisine', views.cuisine),
    path('cuisine_show', views.cuisine_show),
    path('cuisine_edit/<int:id>', views.cuisine_edit),
    path('cuisine_update/<int:id>', views.cuisine_update),
    path('cuisine_delete/<int:id>', views.cuisine_delete),
    path('dish/<int:cuisine_id>', views.dish, name='insert'),
    path('dish_show/<int:cuisine_id>', views.dish_show, name='display'),
    path('dish_edit/<int:id>', views.dish_edit),
    path('dish_update/<int:id>', views.cuisine_update),
    path('dish_delete/<int:id>', views.dish_delete),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)