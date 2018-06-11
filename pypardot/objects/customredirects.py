class CustomRedirects():
    """
    A class to query and use Pardot visitors.
    Visitor field reference: http://developer.pardot.com/kb/api-version-3/object-field-references#visitor
    """

    def __init__(self, client):
        self.client = client

    def query(self, **kwargs):
        """
        Returns the cutomRedirects matching the specified criteria parameters.
        Supported search criteria: http://developer.pardot.com/kb/api-version-3/querying-visitors#supported-search-criteria-
        """
        result = self._get(path='/do/query', params=kwargs)
        return result.get('result')

    def _get(self, object='customRedirect', path=None, params=None):
        """GET requests for the CustomRedirect object."""
        if params is None:
            params = {}
        result = self.client.get(object=object, path=path, params=params)
        return result

    def _post(self, object='customRedirect', path=None, params=None):
        """POST requests for the CustomRedirect object."""
        if params is None:
            params = {}
        result = self.client.post(object=object, path=path, params=params)
        return result

