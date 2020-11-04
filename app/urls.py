from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.home, name='home'),
    path('Buy/Tickets', views.payments, name='Buy/Tickets'),
    path('Membership', views.membership, name='Membership'),
    path('Activities', views.activities, name='Activities'),
    path('BushCamps', views.bushcamps, name='BushCamps'),
    path('Species', views.species, name='Species'),
    path('Gallery', views.gallery, name='Gallery'),
    path('EcoSchool', views.ecoschool, name='EcoSchool'),
    path('Supporters', views.supporters, name='Supporters'),
    path('Contact', views.contactUs, name='Contact'),
    path('Blog', views.blog, name='Blog'),
    path('Events', views.events, name='Events'),
    path('Shop', views.shop, name='Shop'),
    path('Map', views.map, name='Map'),
    path('signup',views.signup,name="signup"),
    
] 
