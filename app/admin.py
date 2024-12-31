from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Rating)
class RatingAdmin(admin.ModelAdmin):
    pass
