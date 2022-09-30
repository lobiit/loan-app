from django.contrib.auth import views as auth_views
from django.urls import path
from core import views as core_views
from core.views import  Index, Show

urlpatterns = [
    path('', core_views.home, name='home'),
    path('index/', Index.as_view(), name='Index'),
    path('show/', Show.as_view(), name='show')

]
