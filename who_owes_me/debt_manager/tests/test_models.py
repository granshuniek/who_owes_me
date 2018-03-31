from django.test import TestCase
from debt_manager.models import Debtors, Creditors, Debts
from datetime import datetime

# django tests run: python manage.py test debt_manager.tests

class DebtsTestCase(TestCase):

    @classmethod
    def setUpTestData(self):
        debtor1 = Debtors.objects.create(first_name="Jan", last_name="Kowalski")
        debtor2 = Debtors.objects.create(first_name="Aleksander", last_name="Wielki")
        debtor3 = Debtors.objects.create(first_name="Piotruś", last_name="Pan")

        creditor1 = Creditors.objects.create(first_name="Andrzej", last_name="Grabowski")
        creditor2 = Creditors.objects.create(first_name="Quentin", last_name="Tarantino")
        # creditor3 = Creditors.objects.create(first_name="Sherlock", last_name="Holmes")

        Debts.objects.create(debtor=debtor1, creditor=creditor1,
                             amount=100, for_what='asd', description='asdffds',
                             date=datetime.now())
        
        Debts.objects.create(debtor=debtor1, creditor=creditor1,
                             amount=100, for_what='asd', description='asdffds',
                             date=datetime.now())
        
        Debts.objects.create(debtor=debtor3, creditor=creditor2,
                             amount=50, for_what='asd', description='asdffds',
                             date=datetime.now())

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_set_up_data(self):
        amount = Debts.objects.get(id=1).amount
        self.assertTrue(100, amount)

    def test_creditor_charges_sum(self):
        test_charges_dict = {1: 200.0,
                             2: 50.0}
        
        charges_sum = Creditors.objects.get_creditor_charges_sum()
        self.assertEqual(test_charges_dict, charges_sum)

    def test_debtors_debts_sum(self):
        test_charges_dict = {1: 200.0,
                             2: 50.0}
        charges_sum = Creditors.objects.get_creditor_charges_sum()
        self.assertEqual(test_charges_dict, charges_sum)