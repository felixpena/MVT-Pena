from django.contrib import admin
from django.urls import include, path
from familia import views

urlpatterns = [
    path('', views.inicio),
    path('familia/', include('familia.urls')),
    path('admin/', admin.site.urls),
    

]