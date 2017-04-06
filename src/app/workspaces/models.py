from django.db import models
from tunobase.core import models as core_models

# Create your models here.
class Workspaces(core_models.BaseContentModel):
    pass

    class Meta:
        verbose_name = 'Workspace'
        verbose_name_plural = 'Workspaces'

    def __unicode__(self):
        return self.title
