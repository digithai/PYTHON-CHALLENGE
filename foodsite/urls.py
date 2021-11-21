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
    path('cuisine/', views.cuisine),
    path('dish_show/<int:cuisine_id>', views.dish_show, name='display'),
    path('insert_dish/<int:cuisine_id>',views.insert_dish, name='insert'),
    path('update_cuisine/<int:id>',views.update_cuisine, name='update_cuisine'),
    path('update_dish/<int:id>', views.update_dish, name='update_dish'),
    path('<id>/delete_dish', views.delete_dish, name='delete_dish'),
    path('<id>/delete_cuisine', views.delete_cuisine, name='delete_cuisine'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)