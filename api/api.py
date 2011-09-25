from tastypie import fields
from tastypie.cache import SimpleCache
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from nskyc.api.models import Pictures, Users

URL_PREFIX = 'http://s3.amazonaws.com/nskyc/'

class LocationResource(ModelResource):
    class Meta:
        queryset = Users.objects.all()
        resource_name = 'location'
        
        filtering = {
            'name': ALL
        }

        cache = SimpleCache()
        default_format = 'application/json'


class PictureResource(ModelResource):
    location = fields.ForeignKey(LocationResource, 'user', full=True)    
    
    class Meta:
        queryset = Pictures.objects.all().order_by('-date_posted')
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = 'picture'

        filtering = {
            'location': ALL_WITH_RELATIONS,
            'date_posted': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
        
        ordering = ['date_posted']
        
        cache = SimpleCache()
        default_format = 'application/json'
             

    def dehydrate_path(self, bundle):
        return "%s%s" % (URL_PREFIX, bundle.data['path'])