from django.db import models, connection

def _execute_sql(sql):
        with connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

class CreditorsAndDebtorsManager(models.Manager):
    """
        Manager for Debtors and Creditors models.
    """
    def get_creditor_charges_sum(self):
        """
        Method sum amount of charges of current creditor.
        
        :returns: return_dict
            { creditor_id: sumed_charge }
        """

        sql = '''
            SELECT crds.id, sum(dts.amount)
            FROM debt_manager_debts dts
            JOIN debt_manager_creditors crds on crds.id=dts.creditor_id
            GROUP BY crds.id
        '''
        response = _execute_sql(sql)
        return_dict = {}
        for creditor_id, sumed_charge in response:
            return_dict[creditor_id] = sumed_charge
        return return_dict    

    def get_debtor_debts_sum(self):
        """
        Method sum amount of debts of current debtor.
        
        :returns: return_dict
            { debtor_id: sumed_debt }
        """

        sql = '''
            SELECT dbtr.id, sum(dts.amount)
            FROM debt_manager_debts dts
            JOIN debt_manager_debtors dbtr on dbtr.id=dts.debtor_id
            GROUP BY dbtr.id
        '''
        response = _execute_sql(sql)
        return_dict = {}
        for debtor_id, sumed_debt in response:
            return_dict[debtor_id] = sumed_debt
        return return_dict

class DebtsManager(models.Manager):
    def get_current_user_debts(self, id):
        users_debts = {}
        sql = '''
            SELECT * from debt_manager_debts where 
        '''
        pass