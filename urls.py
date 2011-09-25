from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.views.decorators.cache import cache_page

from tastypie.api import Api
from api.api import PictureResource, LocationResource


v1_api = Api(api_name='v1')
v1_api.register(LocationResource())
v1_api.register(PictureResource())

urlpatterns = patterns('',
    (r'^$', cache_page(60 * 15)(direct_to_template), {'template':'api/index.html'}),
    (r'^styles.css$', cache_page(60 * 15)(direct_to_template), {'template':'api/styles.css', 'mimetype':'text/css'}),
    (r'^api/', include(v1_api.urls)),
)
