from django.shortcuts import render
from django.views import generic
from .models import Debtors, Debts, Creditors

def index(request):
    all_debts = Debts.objects.all()
    context = {
        'debts': all_debts
    }

    return render(request, 'debt_manager/index.html', context)

class DebtListView(generic.ListView):
    model = Debts

class DebtDetailView(generic.DetailView):
    model = Debts


class DebtorListView(generic.ListView):
    model = Debtors

class DebtorDetailView(generic.DetailView):
    model = Debtors


class CreditorListView(generic.ListView):
    model = Debtors

class CreditorDetailView(generic.DetailView):
    model = Debtors