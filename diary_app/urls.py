from django.conf.urls import url
from diary_app import views


urlpatterns = [
    url(r'^$', views.index, name='index'), 
    url(r'^entrylist/', views.EntryList.as_view(), name='entry_list'),
    url(r'^entry/(?P<pk>\d+)$', views.EntryDetail.as_view(), name='entry_detail'),
    url(r'^entry/new/$', views.CreateEntry.as_view(), name='entry_new'),
    url(r'^entry/(?P<pk>\d+)/edit/$', views.UpdateEntry.as_view(), name='entry_update'),
    url(r'^entry/(?P<pk>\d+)/remove/$', views.DeleteEntry.as_view(), name='remove_entry'),
    url(r'^drafts/$', views.DraftList.as_view(), name='entry_draft_list'),

]