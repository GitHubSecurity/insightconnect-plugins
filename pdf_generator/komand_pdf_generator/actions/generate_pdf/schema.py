# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    TEXT = "text"
    

class Output:
    PDF = "pdf"
    

class GeneratePdfInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "text": {
      "type": "string",
      "title": "Text",
      "description": "Text input",
      "order": 1
    }
  },
  "required": [
    "text"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GeneratePdfOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "pdf": {
      "type": "string",
      "title": "PDF",
      "displayType": "bytes",
      "description": "Generated PDF",
      "format": "bytes",
      "order": 1
    }
  },
  "required": [
    "pdf"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
