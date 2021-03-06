import komand
import requests
from .. import demo_test
from .schema import ListDomainRiskRulesInput, ListDomainRiskRulesOutput


class ListDomainRiskRules(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_domain_risk_rules',
                description='This action is used to list available filtration rules for domain risk lists',
                input=ListDomainRiskRulesInput(),
                output=ListDomainRiskRulesOutput())

    def run(self, params={}):
        try:
            risklist = params.get("list")
            query_headers = {'X-RFToken': self.connection.token}
            results = requests.get("https://api.recordedfuture.com/v2/domain/riskrules", headers=query_headers).json()
            return {"risk_rules": results["data"]["results"]}
        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        return demo_test.demo_test(self.connection.token, self.logger)
