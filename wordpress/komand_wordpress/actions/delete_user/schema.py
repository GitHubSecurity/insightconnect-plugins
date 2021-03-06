# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    REASSIGNEE = "reassignee"
    USERNAME = "username"
    

class Output:
    SUCCESS = "success"
    

class DeleteUserInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "reassignee": {
      "type": "string",
      "title": "Reassignee",
      "description": "Username to reassign posts to",
      "order": 2
    },
    "username": {
      "type": "string",
      "title": "Username",
      "description": "Username",
      "order": 1
    }
  },
  "required": [
    "username",
    "reassignee"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteUserOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "User Deleted",
      "description": "User Deleted",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
