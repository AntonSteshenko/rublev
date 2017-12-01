from django.contrib import admin
from organizations.models import Organization, Doc, Office

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["short_name"]

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Doc)
admin.site.register(Office)

