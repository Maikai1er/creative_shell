from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('update_data/', views.update_data, name='update_data'),
    path('', views.index, name='home'),
    path('load-more-heritages/', views.load_more_heritages, name='load_more_heritages',),
    path('get_next_heritage/', views.get_next_heritage, name='get_next_heritage'),
    path('save_heritage/', views.save_heritage, name='save_heritage'),
    path('receive_contact_data/', views.receive_contact_data, name='receive_contact_data'),
]
