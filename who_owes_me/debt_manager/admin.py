from django.contrib import admin
from .models import Debtors, Debts, Creditors, User

admin.site.register(Debtors)
admin.site.register(Creditors)
admin.site.register(Debts)
admin.site.register(Debts)
admin.site.register(User, UserAdmin)