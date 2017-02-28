from django.contrib import admin

# Register your models here.
from log.models import Step, MyUser



class StepsAdmin(admin.ModelAdmin):
    list_display = ('user','steps','insertion_date')

admin.site.register(MyUser)
admin.site.register(Step, StepsAdmin)

