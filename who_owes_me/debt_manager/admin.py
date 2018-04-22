from django.contrib import admin
from .models import Debtors, Debts, Creditors, Profile
from django.contrib.auth.admin import UserAdmin

admin.site.register(Debtors)
admin.site.register(Creditors)
admin.site.register(Debts)
admin.site.register(Profile, UserAdmin)
