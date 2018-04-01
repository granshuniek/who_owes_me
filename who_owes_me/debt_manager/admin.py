from django.contrib import admin
from .models import Debtors, Debts, Creditors

admin.site.register(Debtors)
admin.site.register(Creditors)
admin.site.register(Debts)