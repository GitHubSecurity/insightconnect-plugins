# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    AS = "as"
    LIMIT = "limit"
    

class Output:
    RESULTS = "results"
    

class AsnInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "as": {
      "type": "string",
      "title": "AS Number",
      "description": "Autonomous System Number",
      "order": 1
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "description": "Limit number of results",
      "order": 2
    }
  },
  "required": [
    "as",
    "limit"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AsnOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "type": "array",
      "title": "Results List",
      "description": "Results list",
      "items": {
        "$ref": "#/definitions/detailed"
      },
      "order": 1
    }
  },
  "definitions": {
    "detailed": {
      "type": "object",
      "title": "detailed",
      "properties": {
        "as": {
          "type": "string",
          "title": "AS",
          "description": "AS",
          "order": 8
        },
        "country": {
          "type": "string",
          "title": "Country code",
          "description": "Country code",
          "order": 9
        },
        "date": {
          "type": "string",
          "title": "Date",
          "displayType": "date",
          "description": "Date",
          "format": "date-time",
          "order": 1
        },
        "guid": {
          "type": "string",
          "title": "GUID",
          "description": "ZeuS tracker GUID",
          "order": 11
        },
        "host": {
          "type": "string",
          "title": "Host",
          "description": "Host",
          "order": 2
        },
        "ip": {
          "type": "string",
          "title": "IP",
          "description": "IP address",
          "order": 3
        },
        "level": {
          "type": "integer",
          "title": "Level",
          "description": "Level",
          "order": 6
        },
        "link": {
          "type": "string",
          "title": "Link",
          "description": "ZeuS tracker information link",
          "order": 10
        },
        "malware": {
          "type": "string",
          "title": "Malware",
          "description": "Malware name",
          "order": 7
        },
        "sbl": {
          "type": "string",
          "title": "SBL",
          "description": "SBL",
          "order": 4
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status",
          "order": 5
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
