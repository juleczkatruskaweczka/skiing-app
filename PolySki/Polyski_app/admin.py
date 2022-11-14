from django.contrib import admin
from Polyski_app.models import AccessRecord, Topic, Webpage, User
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)
admin.site.register(User)
