# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    SCAN_CONFIG_ID = "scan_config_id"
    

class Output:
    STATUS = "status"
    

class DeleteScanConfigInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "scan_config_id": {
      "type": "string",
      "title": "Scan Config ID",
      "description": "Scan configuration UUID",
      "order": 1
    }
  },
  "required": [
    "scan_config_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteScanConfigOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "integer",
      "title": "Status",
      "description": "Status code of the request",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
