# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    QUERY = "query"
    

class Output:
    ANALYSES = "analyses"
    

class SearchAnalysisInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "query": {
      "type": "string",
      "title": "Query",
      "description": "String to search for",
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


class SearchAnalysisOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "analyses": {
      "type": "array",
      "title": "Analyses",
      "description": "A list of matching analyses IDs",
      "items": {
        "$ref": "#/definitions/webid"
      },
      "order": 1
    }
  },
  "required": [
    "analyses"
  ],
  "definitions": {
    "webid": {
      "type": "object",
      "title": "webid",
      "properties": {
        "webid": {
          "type": "string",
          "title": "WebID",
          "description": "Web ID",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
