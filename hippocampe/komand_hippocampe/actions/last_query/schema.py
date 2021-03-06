# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    pass

class Output:
    LAST_QUERIES = "last_queries"
    

class LastQueryInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class LastQueryOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "last_queries": {
      "type": "array",
      "title": "Last Queries",
      "description": "List of last query times for every source",
      "items": {
        "$ref": "#/definitions/last_query"
      },
      "order": 1
    }
  },
  "required": [
    "last_queries"
  ],
  "definitions": {
    "last_query": {
      "type": "object",
      "title": "last_query",
      "properties": {
        "lastQuery": {
          "type": "string",
          "title": "Last Query",
          "displayType": "date",
          "description": "Last query time",
          "format": "date-time",
          "order": 2
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "Source (e.g. URL)",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
