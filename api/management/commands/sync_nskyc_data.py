from datetime import timedelta

from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand

from nskyc.api.models import Pictures, Users

"""
sync_nskyc_data
Updated 9/24/2011, Joshua Ruihley

grabs latest pictures from nskyc and stores in local db
"""

class Command(NoArgsCommand):
    
    
    def handle_noargs(self, **options):
        latest_time = Pictures.objects.using('default').all().order_by('-date_posted')[0].date_posted
        d = timedelta(hours=7)
        latest_time = latest_time - d
        print latest_time
        new_pics = Pictures.objects.using('master').filter(date_posted__gt=latest_time)
        for p in new_pics:
            p.pk=None
            p.date_posted=p.date_posted + d
            p.save(using='default')