# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

class CreditorBankAccount(object):
    """A thin wrapper around a creditor_bank_account, providing easy access to its
    attributes.

    Example:
      creditor_bank_account = client.creditor_bank_accounts.get()
      creditor_bank_account.id
    """

    def __init__(self, attributes, api_response):
        self.attributes = attributes
        self.api_response = api_response

    @property
    def account_holder_name(self):
        return self.attributes.get('account_holder_name')

    @property
    def account_number_ending(self):
        return self.attributes.get('account_number_ending')

    @property
    def bank_name(self):
        return self.attributes.get('bank_name')

    @property
    def country_code(self):
        return self.attributes.get('country_code')

    @property
    def created_at(self):
        return self.attributes.get('created_at')

    @property
    def currency(self):
        return self.attributes.get('currency')

    @property
    def enabled(self):
        return self.attributes.get('enabled')

    @property
    def id(self):
        return self.attributes.get('id')

    @property
    def links(self):
        return self.Links(self.attributes.get('links'))

    @property
    def metadata(self):
        return self.attributes.get('metadata')

    class Links(object):
        """Wrapper for the response's 'links' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes

        @property
        def creditor(self):
            return self.attributes.get('creditor')

