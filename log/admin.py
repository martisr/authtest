from django.contrib import admin

# Register your models here.
from log.models import Step, MyUser

admin.site.register(MyUser)
admin.site.register(Step)