from django.shortcuts import render
from django.views import generic
from .models import Debtors, Debts, Creditors, Profile
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    context = {}
    return render(request, 'debt_manager/index.html', context)

class DebtListView(LoginRequiredMixin, generic.ListView):
    model = Debts

class DebtDetailView(LoginRequiredMixin, generic.DetailView):
    model = Debts

class DebtorListView(LoginRequiredMixin, generic.ListView):
    model = Debtors

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['debts_sums'] = self.model.objects.get_debtor_debts_sum()
        context['charges_sums'] = self.model.objects.get_creditor_charges_sum()
        return context

class DebtorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Debtors

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['debts_sums'] = self.model.objects.get_debtor_debts_sum()
        return context

class CreditorListView(LoginRequiredMixin, generic.ListView):
    model = Creditors
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['charges_sums'] = self.model.objects.get_creditor_charges_sum()
        return context

class CreditorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Creditors

class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    model = Profile