from django.test import TestCase
from debt_manager.models import Debtors, Creditors, Debts
from datetime import datetime

class DebtsTestCase(TestCase):
    
    @classmethod
    def setUpTestData(self):
        debtor = Debtors.objects.create(first_name="Jan", last_name="Kowalski")
        creditor = Creditors.objects.create(first_name="Andrzej", last_name="Grabowski")
        Debts.objects.create(debtor=debtor, creditor=creditor,
                             amount=100, for_what='asd', description='asdffds',
                             date=datetime.now())
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_set_up_data(self):
        amount = Debts.objects.get(id=1).amount
        self.assertTrue(100, amount)