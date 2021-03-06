# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    INCIDENT_ID = "incident_id"
    ORGANIZATION_ID = "organization_id"
    

class Output:
    STATUS = "status"
    

class DeleteIncidentInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "incident_id": {
      "type": "number",
      "title": "Incident ID",
      "description": "The incident ID",
      "order": 2
    },
    "organization_id": {
      "type": "number",
      "title": "Organization ID",
      "description": "The organization ID",
      "order": 1
    }
  },
  "required": [
    "organization_id",
    "incident_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteIncidentOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "$ref": "#/definitions/StatusDTO",
      "title": "Status",
      "description": "Status",
      "order": 1
    }
  },
  "definitions": {
    "StatusDTO": {
      "type": "object",
      "title": "StatusDTO",
      "properties": {
        "hints": {
          "type": "array",
          "title": "Hints",
          "items": {
            "type": "string"
          },
          "order": 4
        },
        "message": {
          "type": "string",
          "title": "Message",
          "order": 3
        },
        "success": {
          "type": "boolean",
          "title": "Success",
          "order": 1
        },
        "title": {
          "type": "string",
          "title": "Title",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
