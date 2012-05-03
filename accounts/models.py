from django.db import models

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=255,verbose_name="Account Name")
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
#    date_created = models.DateTimeField(auto_now_add=True)
#    date_last_modfied = models.DateTimeField(auto_now=True)
#    date_last_accessed = models.DateTimeField()


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]
    