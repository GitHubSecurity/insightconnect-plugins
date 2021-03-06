# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    AGENT_ID = "agent_id"
    

class Output:
    ERROR = "error"
    MESSAGE = "message"
    

class AgentScanInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent_id": {
      "type": "string",
      "title": "Agent ID",
      "description": "Agent ID e.g. 003. If no agent is specified, scans will take place on all agents",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AgentScanOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "error": {
      "type": "integer",
      "title": "Error code",
      "description": "Error code",
      "order": 2
    },
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Status message",
      "order": 1
    }
  },
  "required": [
    "message",
    "error"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
