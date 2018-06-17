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

    def get_current_user_dict_of_debts(self, user_id):
        pass

    # def get_current_user_dict_of_debts(self, user_id):
    #     user_profile_id = self._get_user_profile_id(user_id)
    #     debts_sql = '''
    #         SELECT * from debt_manager_debts where debtor_id={0}
    #     '''.format(user_id)
    #     users_debt_list = []
    #     current_user_debts = _execute_sql(debts_sql)
    #     for debt in current_user_debts:
    #         debt_dict = {}
    #         debt_dict['id'] = debt[0]
    #         debt_dict['amount'] = debt[1]
    #         debt_dict['for_what'] = debt[2]
    #         debt_dict['date'] = debt[4]
    #         auth_user_info = self._get_user_auth_info("debt_manager_creditors", debt[5])
    #         debt_dict['creditor'] = "{0} {1}".format(auth_user_info[1], auth_user_info[2])
    #         users_debt_list.append(debt_dict)
    #     return users_debt_list
    #
    # def _get_user_auth_info(self, first_table, user_profile_id):
    #     first_table_sql = 'SELECT user_id FROM {0} WHERE id={1}'.format(first_table, user_profile_id)
    #     first_table_user_id = _execute_sql(first_table_sql)[0][0]
    #     user_auth_id_sql = 'SELECT user_id FROM debt_manager_profile WHERE id={0}'.format(first_table_user_id)
    #     user_auth_id = _execute_sql(user_auth_id_sql)[0][0]
    #
    #     user_auth_info_sql = '''
    #         SELECT username, first_name, last_name, email FROM auth_user WHERE id={0}
    #     '''.format(user_auth_id)
    #
    #     user_auth_info = _execute_sql(user_auth_info_sql)[0]
    #
    #     return user_auth_info
    #
    # def _get_user_profile_id(self, user_id):
    #     sql = "SELECT id from debt_manager_profile WHERE user_id={0}".format(user_id)
    #     return _execute_sql(sql)[0][0]