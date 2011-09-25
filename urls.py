from django.conf.urls.defaults import patterns, include, url
from api.api import PictureResource, LocationResource
from tastypie.api import Api


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(LocationResource())
v1_api.register(PictureResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nskyc.views.home', name='home'),
    # url(r'^nskyc/', include('nskyc.foo.urls')),
    (r'^api/', include(v1_api.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
