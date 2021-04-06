from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Contact

class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...

admin.site.register(Contact, ContactAdmin)