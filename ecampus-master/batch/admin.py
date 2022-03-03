from django.contrib import admin

from .models import Batch, BatchDetail, BatchTime

# Register your models here.
admin.site.register(Batch)
admin.site.register(BatchDetail)
admin.site.register(BatchTime)
