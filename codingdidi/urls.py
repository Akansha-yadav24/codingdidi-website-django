from django.urls import path
from homepage import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.index, name='index'),
    path('powerbi/', views.powerbi, name='powerbi'),
    path('signup/', views.signup, name='signup'),# Add this line if it doesn't exist
    path('login/', views.login_view, name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
