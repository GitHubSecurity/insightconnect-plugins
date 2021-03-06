# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    TIME = "time"
    

class Output:
    SCHEDULE = "schedule"
    

class HipposchedInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "time": {
      "type": "string",
      "title": "Time",
      "description": "Job frequency in crontab syntax, e.g. `* */12 * * *`",
      "order": 1
    }
  },
  "required": [
    "time"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class HipposchedOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "schedule": {
      "type": "string",
      "title": "Schedule",
      "description": "Newly set job frequency",
      "order": 1
    }
  },
  "required": [
    "schedule"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
