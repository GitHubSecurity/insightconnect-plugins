import komand
from .schema import UpdateSiteIncludedTargetsInput, UpdateSiteIncludedTargetsOutput, Input, Output
# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_helper import ResourceHelper


class UpdateSiteIncludedTargets(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_site_included_targets',
                description='Update an existing site scope of included ip address and hostname targets',
                input=UpdateSiteIncludedTargetsInput(),
                output=UpdateSiteIncludedTargetsOutput())

    def run(self, params={}):
        scope = params.get(Input.INCLUDED_TARGETS)
        resource_helper = ResourceHelper(self.connection.session, self.logger)
        endpoint = endpoints.Site.site_included_targets(self.connection.console_url, params.get(Input.ID))

        # Pull current site scope in order to append to list instead of overwriting
        if not params.get(Input.OVERWRITE):
            current_scope = resource_helper.resource_request(endpoint=endpoint,
                                                             method='get')
            self.logger.info(f"Appending to current list of included targets")
            scope.extend(current_scope['addresses'])

        self.logger.info(f"Using {endpoint} ...")
        response = resource_helper.resource_request(endpoint=endpoint,
                                                    method='put',
                                                    payload=scope)

        return {
            "id": params.get(Input.ID),
            "links": response['links']
        }
