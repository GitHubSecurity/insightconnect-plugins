# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    CIDR = "cidr"
    

class Output:
    IS_BLOCKED = "is_blocked"
    RESULT = "result"
    

class QueryInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "cidr": {
      "type": "string",
      "title": "CIDR",
      "description": "IP Address or CIDR network to block",
      "order": 1
    }
  },
  "required": [
    "cidr"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class QueryOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "is_blocked": {
      "type": "boolean",
      "title": "Blocked",
      "description": "Blocked",
      "order": 2
    },
    "result": {
      "type": "array",
      "title": "Block List",
      "description": "Block List",
      "items": {
        "type": "object"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
