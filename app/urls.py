from django.urls.conf import path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from app import views

'''
urlpatterns = [
    path("", views.index , name="about"),
    path('webhook/', csrf_exempt(views.webhook), name='dialogflow-webhook'), 
    path('nav/', TemplateView.as_view(template_name='layout/nav_bootstrap3.html'), name='navigator'),
    path('identity/',views.AiIdentityListView.as_view(), name='identity'),
    path('identity/<slug:pk>/detail/',views.api_ai_identity_detail, name='identity-detail'),
    path('foresty/create', views.api_ai_identity, name='identity-create'),
    path('simulation/', TemplateView.as_view(template_name='agent/simulation.html'), name='simulation'),
    
    
    path('clear_easyai/', views.web_api_init_easyai, name='clear-easyai'),

]
'''



