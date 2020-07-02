from django.contrib import admin
from HTech.models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources




class UserResurce(resources.ModelResource):

    class Meta:
        model = User

#Add user Class csv
@admin.register(User)
class AddUser(ImportExportActionModelAdmin):
    resource_class = UserResurce
    list_display =[field.name for field in User._meta.fields]
    search_fields = ["FirstName", "LastName", "Country", "Email"]
    fieldsets = (
        (None, {
            'fields': ('FirstName', 'LastName', 'Country', 'Email','PhoneNumber')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('Status',)
        }),
    )








