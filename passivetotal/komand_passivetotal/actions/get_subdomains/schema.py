# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    QUERY = "query"
    

class Output:
    COUNT = "count"
    SUBDOMAINS = "subdomains"
    

class GetSubdomainsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "query": {
      "type": "string",
      "title": "Query",
      "description": "Input query, e.g. *.passivetotal.org",
      "order": 1
    }
  },
  "required": [
    "query"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetSubdomainsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "count": {
      "type": "integer",
      "title": "Count",
      "description": "Number of results returned",
      "order": 1
    },
    "subdomains": {
      "type": "array",
      "title": "Subdomains",
      "description": "Subdomains returned, e.g [foo, bar, api]",
      "items": {
        "type": "string"
      },
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
