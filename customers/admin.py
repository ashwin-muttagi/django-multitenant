
from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Domain, Client


class DomainInline(admin.TabularInline):

    model = Domain
    max_num = 1


@admin.register(Client)
class TenantAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = (
        "user",
        "is_active",
        "created_on",
        )
        inlines = [DomainInline]
