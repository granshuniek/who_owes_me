from django.db import models, connection

CREDITOR = 'creditor'
DEBTOR = 'debtor'

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

    def get_current_user_dict_of_debts(self, users_id):
        sql = '''
            SELECT * from debt_manager_debts where debtor_id={0}
        '''.format(users_id)
        users_debt_list = []
        response = _execute_sql(sql)
        for row in response:
            debt_dict = {}
            debt_dict['id'] = row[0]
            debt_dict['amount'] = row[1]
            debt_dict['for_what'] = row[2]
            debt_dict['date'] = row[4]
            creditor_tuple = _get_creditor_or_debtor_info(CREDITOR, row[5])
            debt_dict['creditor'] = "{0} {1}".format(creditor_tuple[0], creditor_tuple[1])
            users_debt_list.append(debt_dict)
        return users_debt_list

def _get_creditor_or_debtor_info(person_type, creditor_id):
    user_profile_sql = 'SELECT user_id FROM debt_manager_creditors WHERE id={0}'.format(creditor_id)
    user_profile_id = _execute_sql(user_profile_sql)[0][0]
    aut_user_sql = 'SELECT user_id FROM debt_manager_profile WHERE id={0}'.format(user_profile_id)
    auth_user_id = _execute_sql(aut_user_sql)[0][0]
    auth_user_info_sql = 'SELECT first_name, last_name, username FROM auth_user WHERE id={0}'.format(auth_user_id)
    return _execute_sql(auth_user_info_sql)[0]