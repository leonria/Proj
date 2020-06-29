from django.contrib import admin
from HTech.models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget
class UserResurce(resources.ModelResource):

    class Meta:
        model = User

#Add user Class csv
class AddUser(ImportExportActionModelAdmin):
    resource_class = UserResurce
    list_display =[field.name for field in User._meta.fields]
    search_fields = ["FirstName", "LastName", "Country", "Email"]
admin.site.register(User,AddUser)

#Add user Class
'''class AddUser(admin.ModelAdmin):
    list_display =[field.name for field in User._meta.fields]
    search_fields = ["FirstName","LastName","Country","Email"]

    class Meta:
        model = User


# Register your models here.
admin.site.register(User,AddUser)'''

#Add Twilio Class
class AddTwillo(admin.ModelAdmin):
    list_display =[field.name for field in Twillo._meta.fields]
    search_fields = ["AccountName","Phone","Email","account_sid"]

    class Meta:
        model = Twillo

# Register your models here.
admin.site.register(Twillo,AddTwillo)

#Add Server Status Class
class ServerStat(admin.ModelAdmin):
    list_display =[field.name for field in ServerStatus._meta.fields]
    search_fields = ["ServerName","Status"]

    class Meta:
        model = ServerStatus

# Register your models here.
admin.site.register(ServerStatus,ServerStat)

