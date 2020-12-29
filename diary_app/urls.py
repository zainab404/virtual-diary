from django.conf.urls import url
from diary_app import views

app_name = 'diary_app'

urlpatterns = [
    url(r'^$', views.index, name='index'), 
    url(r'^new_entry/', views.EntryList.as_view(), name='new_entry'),
    url(r'')
]