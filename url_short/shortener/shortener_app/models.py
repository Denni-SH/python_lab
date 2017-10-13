from django.db import models
import hashlib
from .validator import validate_url


class UrlsManager(models.Manager):
    def all(self,*args,**kwargs):
        qs_main = super(UrlsManager,self).all(*args,**kwargs)
        qs = qs_main.filter(active=True)
        return qs

    # def refresh_shortcodes(self,items=None):
    #     qs = Urls.objects.filter(id__gte=1)
    #     if items is not None and isinstance(items,int):
    #         qs = qs.order_by('-id')[:items]
    #     new_codes = 0
    #     for q in qs:
    #         q.short_url = hashlib.md5(self.url).hexdigest()
    #         q.save()
    #         new_codes+=1
    #     return 'New codes made: %s' %new_codes


class Urls(models.Model):
    url = models.CharField(max_length=220, validators=[validate_url])
    short_url = models.CharField(max_length=32, default=None,unique=True,blank=True)
    # updated = models.DateTimeField(auto_now=True)
    # timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    objects = UrlsManager()
    def save(self,*args,**kwargs):
        if self.short_url is None or self.short_url == "":
            self.short_url = hashlib.md5(self.url).hexdigest()
        super(Urls,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

