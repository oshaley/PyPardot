class EmailTemplates():
    """
    A class to query and use Pardot visitors.
    Visitor field reference: http://developer.pardot.com/kb/api-version-3/object-field-references#visitor
    """

    def __init__(self, client):
        self.client = client

    def query_by_ids(self, ids=None, **kwargs):
        """Returns the Email Templates matching the given <ids>. The <ids> should be comma separated integers (no spaces)."""
        # kwargs['ids'] = ids.replace(' ', '')
        templates = []
        for k in ids:
            path = '/do/read/id/'+str(k)
            result = self._get(path=path, params=kwargs)
            template = result.get('emailTemplate')
            templates.append(template)
        return templates

    def query_list_one_to_one(self, **kwargs):
        """
        Returns the cutomRedirects matching the specified criteria parameters.
        Supported search criteria: http://developer.pardot.com/kb/api-version-3/querying-visitors#supported-search-criteria-
        """
        result = self._get(path='/do/query', params=kwargs)
        return result.get('result')

    def _get(self, object='emailTemplate', path=None, params=None):
        """GET requests for the EmailTemplate object."""
        if params is None:
            params = {}
        result = self.client.get(object=object, path=path, params=params)
        return result

    def _post(self, object='emailTemplate', path=None, params=None):
        """POST requests for the EmailTemplate object."""
        if params is None:
            params = {}
        result = self.client.post(object=object, path=path, params=params)
        return result

