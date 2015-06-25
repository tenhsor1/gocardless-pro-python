# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources

class PaymentsService(base_service.BaseService):
    """Service class that provides access to the payments
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.Payment
    RESOURCE_NAME = 'payments'

    def create(self, params=None):
        """Create a payment.

        <a name="mandate_is_inactive"></a>Creates a new payment object.
       
        
        This fails with a `mandate_is_inactive` error if the linked
        [mandate](#core-endpoints-mandates) is cancelled. Payments can be
        created against `pending_submission` mandates, but they will not be
        submitted until the mandate becomes active.

        Args:
          params (dict, optional): Request body.

        Returns:
          Payment
        """
        path = '/payments'
        response = self._perform_request('POST', path, params)
        return self._resource_for(response)

    def list(self, params=None):
        """List payments.

        Returns a [cursor-paginated](#overview-cursor-pagination) list of your
        payments.

        Args:
          params (dict, optional): Query string parameters.

        Returns:
          ListResponse of Payment instances
        """
        path = '/payments'
        response = self._perform_request('GET', path, params)
        return self._resource_for(response)

    def get(self, identity, params=None):
        """Get a single payment.

        Retrieves the details of a single existing payment.

        Args:
          identity (string): Unique identifier, beginning with "PM"
          params (dict, optional): Query string parameters.

        Returns:
          Payment
        """
        path = self._sub_url_params('/payments/:identity', {
            'identity': identity,
        })
        response = self._perform_request('GET', path, params)
        return self._resource_for(response)

    def update(self, identity, params=None):
        """Update a payment.

        Updates a payment object. This accepts only the metadata parameter.

        Args:
          identity (string): Unique identifier, beginning with "PM"
          params (dict, optional): Request body.

        Returns:
          Payment
        """
        path = self._sub_url_params('/payments/:identity', {
            'identity': identity,
        })
        response = self._perform_request('PUT', path, params)
        return self._resource_for(response)

    def cancel(self, identity, params=None):
        """Cancel a payment.

        Cancels the payment if it has not already been submitted to the banks.
        Any metadata supplied to this endpoint will be stored on the payment
        cancellation event it causes.
        
        This will fail with a
        `cancellation_failed` error unless the payment's status is
        `pending_submission`.

        Args:
          identity (string): Unique identifier, beginning with "PM"
          params (dict, optional): Request body.

        Returns:
          Payment
        """
        path = self._sub_url_params('/payments/:identity/actions/cancel', {
            'identity': identity,
        })
        response = self._perform_request('POST', path, params)
        return self._resource_for(response)

    def retry(self, identity, params=None):
        """Retry a payment.

        <a name="retry_failed"></a>Retries a failed payment if the underlying
        mandate is active. You will receive a `resubmission_requested` webhook,
        but after that retrying the payment follows the same process as its
        initial creation, so you will receive a `submitted` webhook, followed
        by a `confirmed` or `failed` event. Any metadata supplied to this
        endpoint will be stored against the payment submission event it
        causes.
        
        This will return a `retry_failed` error if the
        payment has not failed.
        
        Payments can be retried up to
        3 times.

        Args:
          identity (string): Unique identifier, beginning with "PM"
          params (dict, optional): Request body.

        Returns:
          Payment
        """
        path = self._sub_url_params('/payments/:identity/actions/retry', {
            'identity': identity,
        })
        response = self._perform_request('POST', path, params)
        return self._resource_for(response)

