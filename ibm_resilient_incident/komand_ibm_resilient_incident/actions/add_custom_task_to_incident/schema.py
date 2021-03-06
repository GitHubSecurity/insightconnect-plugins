# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    BODY = "body"
    INCIDENT_ID = "incident_id"
    ORGANIZATION_ID = "organization_id"
    

class Output:
    IDENTIFIER = "identifier"
    

class AddCustomTaskToIncidentInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "body": {
      "type": "object",
      "title": "Body",
      "description": "Accepts a TaskDTO JSON object. Please see the TaskDTO JSON reference in your Resilient API documentation",
      "order": 3
    },
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
    "incident_id",
    "body",
    "organization_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddCustomTaskToIncidentOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "identifier": {
      "type": "number",
      "title": "Identifier",
      "description": "Identifier",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
