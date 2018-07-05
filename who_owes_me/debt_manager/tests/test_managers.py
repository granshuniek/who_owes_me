from django.test import TestCase
import debt_manager.managers as managers


# django tests run: python manage.py test debt_manager.tests

class ManagersTestCase(TestCase):
    def test_get_debtor_id(self):
        person_type = 'debtor'
        user_id = 1
        managers._execute_sql = self.stub_execute_sql_return_good_id
        return_id = managers._get_debtor_or_creditor_id(person_type, user_id)
        self.assertEqual(return_id, 1)

    def test_get_creditor_id(self):
        person_type = 'creditor'
        user_id = 1
        managers._execute_sql = self.stub_execute_sql_return_good_id
        return_id = managers._get_debtor_or_creditor_id(person_type, user_id)
        self.assertEqual(return_id, 1)

    def test_get_creditor_wrong_empty_ids_list(self):
        person_type = 'creditor'
        user_id = 1
        managers._execute_sql = self.stub_execute_sql_return_empty_list
        return_id = managers._get_debtor_or_creditor_id(person_type, user_id)
        self.assertEqual(return_id, None)

    def test_get_debtor_wrong_empty_ids_list(self):
        person_type = 'debtor'
        user_id = 1
        managers._execute_sql = self.stub_execute_sql_return_empty_list
        return_id = managers._get_debtor_or_creditor_id(person_type, user_id)
        self.assertEqual(return_id, None)

    def stub_execute_sql_return_good_id(self, sql):
        return [(1,),]

    def stub_execute_sql_return_empty_list(self, sql):
        return [(),]
