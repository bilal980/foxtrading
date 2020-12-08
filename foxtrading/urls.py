from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header = 'Fox trading Admin'
admin.site.site_title = 'Fox trading Admin'
admin.site.index_title = "Welcome to Fox trading Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.foxLogin),
    path('signup/', views.foxSignup),
    path('login/', views.handleLogin),
    path('logout/', views.foxLogout),
    path('register/', views.handleSignup),
    path('home/', views.foxHome),
    path('blog/', include('blog.urls')),
    path('trading/', include('trading.urls')),
]
