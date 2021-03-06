# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    USER_ID = "user_id"
    

class Output:
    MESSAGE = "message"
    SUCCESS = "success"
    

class DeleteGlobalUserInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user_id": {
      "type": "integer",
      "title": "User ID",
      "description": "Unique ID of the user eg. 123",
      "order": 1
    }
  },
  "required": [
    "user_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteGlobalUserOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Grafana API response, if any",
      "order": 2
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "True, if the user was deleted",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
