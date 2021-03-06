# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ID = "id"
    PRIORITY = "priority"
    

class Output:
    MESSAGE = "message"
    

class PriorityInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Task ID",
      "order": 1
    },
    "priority": {
      "type": "string",
      "title": "Priority",
      "description": "Task priority from [unbreak, triage, high, normal, low, wish]",
      "order": 2
    }
  },
  "required": [
    "id",
    "priority"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PriorityOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "message": {
      "type": "string",
      "title": "Message",
      "description": "When user is assigned message is: Priority changed",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
