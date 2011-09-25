# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Pictures(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('Users', db_column='uid')
    path = models.CharField(max_length=150)
    color = models.CharField(max_length=24)
    date_posted = models.DateTimeField()
    class Meta:
        db_table = u'pictures'

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, db_column='Name') # Field name made lowercase.
    location = models.CharField(max_length=150, db_column='Location') # Field name made lowercase.
    latitude = models.FloatField()
    longitude = models.FloatField()
    class Meta:
        db_table = u'users'

