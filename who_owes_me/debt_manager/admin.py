from django.contrib import admin
from .models import Debtors, Debts, Creditors

admin.site.register(Debtors)
admin.site.register(Debts)
admin.site.register(Creditors)
