# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    PROJECT_ID = "project_id"
    TOPIC = "topic"
    

class Output:
    TOPIC = "topic"
    

class CreateTopicInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "project_id": {
      "type": "string",
      "title": "Project ID",
      "description": "The project ID for the topic e.g. subpub-1528163449245. If left blank the plugin will use the project ID found in the connection",
      "order": 2
    },
    "topic": {
      "type": "string",
      "title": "Topic",
      "description": "The name of the topic",
      "order": 1
    }
  },
  "required": [
    "topic"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateTopicOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "topic": {
      "type": "string",
      "title": "Topic",
      "description": "Return info on the new topic",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
