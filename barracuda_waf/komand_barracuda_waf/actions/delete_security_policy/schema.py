# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ID = "id"
    

class Output:
    MSG = "msg"
    

class DeleteSecurityPolicyInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "Id",
      "description": "ID of security policy",
      "order": 1
    }
  },
  "required": [
    "id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteSecurityPolicyOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "msg": {
      "type": "string",
      "title": "Msg",
      "description": "Message of update",
      "order": 1
    }
  },
  "required": [
    "msg"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
