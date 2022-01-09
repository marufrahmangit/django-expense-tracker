from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

urlpatterns = [
    path('', include('app.urls')),
    path('login/', views.LoginView.as_view(),name='login'),
    path('logout/', views.LogoutView.as_view(),name='logout',kwargs={'next_page': '/'}),
    path('admin/', admin.site.urls),
]
