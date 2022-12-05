from django.contrib.auth.models import User
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Client(TenantMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)


class Domain(DomainMixin):
    pass