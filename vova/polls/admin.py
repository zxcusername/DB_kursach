from django.contrib import admin

from .models import Dude, Song, Review

# Register your models here.

#admin.site.register(Artist)
admin.site.register(Song)
#admin.site.register(Judge)
admin.site.register(Review)
admin.site.register(Dude)