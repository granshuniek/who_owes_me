from django.db import models, connection

def execute_sql(sql):
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
        response = execute_sql(sql)
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
        response = execute_sql(sql)
        return_dict = {}
        for debtor_id, sumed_debt in response:
            return_dict[debtor_id] = sumed_debt
        return return_dict

class DebtsManager(models.Manager):
    '''
        Manager for class Debts
    '''
    DEBTOR_COLUMN = 'debtor_id'
    CREDITOR_COLUMN = 'creditor_id'

    def get_income_dict(self):
        debts_sql = '''
            SELECT dptr.last_name, dptr.first_name, d.amount
            FROM debt_manager_debts d
            JOIN debt_manager_debtors dptr on dptr.id=d.debtor_id
        '''
        charges_sql = '''
            SELECT crd.last_name, crd.first_name, d.amount
            FROM debt_manager_debts d
            JOIN debt_manager_creditors crd on crd.id=d.creditor_id
        '''
        debt_dict = self._get_payment_dict(debts_sql)
        charge_dict = self._get_payment_dict(charges_sql)
        income_dict = self._count_income_dict(debt_dict, charge_dict)
        return income_dict

    def _count_income_dict(self, debt_dict, charge_dict):
        '''
            If somenoe has debt then it is reduced by charge.            
        '''
        # TODO: case when someone is in charge dict but not in debt dict
        
        for last_name, first_name in debt_dict:
            charge_value = charge_dict.get((last_name, first_name), '')
            if charge_value:
                debt_dict[last_name, first_name] -= float(charge_value)
        return debt_dict

    def _get_payment_dict(self, sql):
        response = execute_sql(sql)
        payment_dict = {}
        for last_name, first_name, amount in response:
            if payment_dict.get((last_name, first_name), ''): 
                payment_dict[last_name, first_name] += amount
            else:
                payment_dict[last_name, first_name] = amount
        return payment_dict

    