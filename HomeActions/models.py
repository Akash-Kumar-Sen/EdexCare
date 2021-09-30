from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse

class HomeActions(models.Model):
    """A typical class defining a model, derived from the Model class."""
    # Fields
    name = models.CharField(max_length=500)
    name_slug=AutoSlugField(populate_from='name')
    description = models.TextField()
    icon_class=models.CharField(max_length=100,default='not assigned')
    hex_color=models.CharField(max_length=20,default='#fc5a03')
    

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('actions', args=[self.name_slug])


class ActionBullet(models.Model):
    Action = models.ForeignKey(HomeActions, default=None, on_delete=models.CASCADE)
    bulletpoint = models.CharField(max_length=500)

    def __str__(self):
        return str(self.Action)

class CustomerResponse(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    whatsapp_number=models.CharField(max_length=20)
    is_interested=models.BooleanField()
    details=models.TextField(blank=True)
    service_required=models.ForeignKey(HomeActions,default=None,on_delete=models.CASCADE)