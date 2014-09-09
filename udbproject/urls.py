from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'udbproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    url(r'^udb/', include('udb.urls', namespace="udb")),
        
        
    url(r'^admin/', include(admin.site.urls)),
    
    
    
    
)
