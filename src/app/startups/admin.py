from django.contrib import admin

# Register your models here.
from app.startups import models


admin.site.register(models.StartupCompanies)