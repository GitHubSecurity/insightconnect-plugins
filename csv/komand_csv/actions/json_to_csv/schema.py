# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    JSON = "json"
    

class Output:
    CSV = "csv"
    

class JsonToCsvInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "json": {
      "type": "array",
      "title": "JSON",
      "description": "JSON array to convert to CSV",
      "items": {
        "type": "object"
      },
      "order": 1
    }
  },
  "required": [
    "json"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class JsonToCsvOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "csv": {
      "type": "string",
      "title": "CSV",
      "displayType": "bytes",
      "description": "Resulting CSV file from the conversion",
      "format": "bytes",
      "order": 1
    }
  },
  "required": [
    "csv"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
