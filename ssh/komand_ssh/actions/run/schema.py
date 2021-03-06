# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    COMMAND = "command"
    HOST = "host"
    

class Output:
    RESULTS = "results"
    

class RunInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "command": {
      "type": "string",
      "title": "Command",
      "description": "Command to execute on remote host",
      "order": 2
    },
    "host": {
      "type": "string",
      "title": "Host",
      "description": "Host to run remote commands. If not provided, the connection host will be used",
      "order": 1
    }
  },
  "required": [
    "command"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RunOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "type": "string",
      "title": "Results",
      "description": "Output results",
      "order": 1
    }
  },
  "required": [
    "results"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
