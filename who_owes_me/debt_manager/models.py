from django.db import models
from django.urls import reverse
from .managers import DebtsManager, CreditorsAndDebtorsManager

class Debtors(models.Model):
    '''
        Model represents people who are owe money.
    '''
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    objects = CreditorsAndDebtorsManager()

    def __str__(self):
        '''
            String representation of model.
        '''
        return '{0} {1}'.format(self.first_name, self.last_name)
    
    def get_absolute_url(self):
        return reverse('debtors-detail', args=[str(self.id)])

class Creditors(models.Model):
    '''
        Model represents people who are creditors.
    '''
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    objects = CreditorsAndDebtorsManager()

    def __str__(self):
        '''
            String representation of model.
        '''
        return '{0} {1}'.format(self.first_name, self.last_name)
    
    def get_absolute_url(self):
        return reverse('creditors-detail', args=[str(self.id)])

class Debts(models.Model):
    '''
        Model represents all debts.
    '''
    debtor = models.ForeignKey('Debtors', on_delete=models.SET_NULL, null=True)
    creditor = models.ForeignKey('Creditors', on_delete=models.SET_NULL, null=True)
    amount = models.FloatField()
    for_what = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    date = models.DateTimeField()
    objects = DebtsManager()

    def __str__(self):
        return "{0} - {1} (date: {2}): {3}".format(self.amount, self.for_what, self.date ,self.description)

    def get_absolute_url(self):
        return reverse('debts-detail', args=[str(self.id)])