from django.db import models
from tunobase.core import models as core_models

# Create your models here.
class Services(core_models.BaseContentModel):
    pass

    def __unicode__(self):
        return self.title
