import komand
from .schema import ResetPasswordInput, ResetPasswordOutput
# Custom imports below
from ldap3 import extend
from komand_active_directory_ldap.util.utils import ADUtils


class ResetPassword(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='reset_password',
                description='Reset a users password',
                input=ResetPasswordInput(),
                output=ResetPasswordOutput())

    def run(self, params={}):
        dn = params.get('distinguished_name')
        dn = ADUtils.dn_normalize(dn)
        temp_list = ADUtils.dn_escape_and_split(dn)
        dn = ','.join(temp_list)
        new_password = params.get('new_password')
        conn = self.connection.conn
        ssl = self.connection.ssl

        if ssl is False:
            raise Exception('SSL must be enabled for the reset password action')

        success = extend.ad_modify_password(conn, dn, new_password, old_password=None)
        result = conn.result

        if success is False:
            raise Exception('something went wrong %s' % result)

        return {'success': success}
