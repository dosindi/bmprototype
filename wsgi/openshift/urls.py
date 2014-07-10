from django.conf.urls import patterns, include, url  
from django.contrib import admin  
from django.conf import settings  
admin.autodiscover()  
urlpatterns = patterns('',  
    # Examples:  
    url(r'^$', 'openshift.views.home', name='home'),  
    url(r'^upload', 'openshift.views.upload_file', name='upload_file'),  
    url(r'^create', 'openshift.views.create_table', name='create_table'),  
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),  
    url(r'^admin/', include(admin.site.urls)),  
) 
