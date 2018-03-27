from django.shortcuts import render
from django.views import generic
from .models import Debtors, Debts, Creditors
from django.db.models import Sum

def index(request):
    all_debts = Debts.objects.all()
    debts_sum = Debts.objects.get_income_dict()
    context = {
        'debts': all_debts,
        'debts_sum': debts_sum,
    }

    return render(request, 'debt_manager/index.html', context)

class DebtListView(generic.ListView):
    model = Debts

class DebtDetailView(generic.DetailView):
    model = Debts

class DebtorListView(generic.ListView):
    model = Debtors
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs) 
    #     return context

class DebtorDetailView(generic.DetailView):
    model = Debtors


class CreditorListView(generic.ListView):
    model = Creditors

class CreditorDetailView(generic.DetailView):
    model = Creditors