# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    COMPARE = "compare"
    LABEL = "label"
    

class Output:
    DIFF = "diff"
    DIFFERENT = "different"
    

class DiffInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "compare": {
      "type": "string",
      "title": "Compare",
      "description": "New data, for comparison against the old data",
      "order": 2
    },
    "label": {
      "type": "string",
      "title": "Cache Label",
      "description": "Unique label to store the old data",
      "order": 1
    }
  },
  "required": [
    "label",
    "compare"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DiffOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "diff": {
      "type": "string",
      "title": "Diff",
      "description": "Diff string",
      "order": 2
    },
    "different": {
      "type": "boolean",
      "title": "Different",
      "description": "True if different",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
