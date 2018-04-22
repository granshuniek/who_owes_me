from django.contrib import admin
from .models import Debtors, Debts, Creditors, UserProfile
from django.contrib.auth.admin import UserAdmin

admin.site.register(Debtors)
admin.site.register(Creditors)
admin.site.register(Debts)
admin.site.register(UserProfile, UserAdmin)
