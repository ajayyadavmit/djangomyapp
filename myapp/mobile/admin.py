from django.contrib import admin

# Register your models here.
from .models import Mobile


class Mobileadmin(admin.ModelAdmin):
    list_display = ('name','cost','location','id')
    list_editable = ('cost',)
    search_fields = ('name',)
    list_filter = ('cost',)

admin.site.register(Mobile,Mobileadmin)

#This admin py file will register the Model created in the Django apps project >> These models will be shown in the SITE LEVLES.. 

# admin.site.register(ClassName)  from .models import classname 

## it shows the app name there.. and you ca perfomr operations thee... 

