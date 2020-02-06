from django.db import models
from django.contrib.auth.models import User
from ..exception_catcher import catch
from django.db import connection


class Subscriber(models.Model):
    subcriber_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=255, null=False, db_index=True)
    phone = models.CharField(max_length=15, null=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    is_active = models.SmallIntegerField(default=1)

    @staticmethod
    @catch(default_value=None)
    def insert(*args, **kwargs):
        records = Subscriber(*args, **kwargs)
        records.save()
        connection.close()
        return records

    @staticmethod
    @catch(default_value=None)
    def select(*args, **kwargs):
        records = Subscriber.objects.filter(*args, *kwargs)
        connection.close()
        return records

    class Meta:
        db_table = 'subscriber'
        ordering = ["-created_date"]
