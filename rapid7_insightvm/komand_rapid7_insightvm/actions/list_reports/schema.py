# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    NAME = "name"
    SORT = "sort"
    

class Output:
    FOUND = "found"
    LIST = "list"
    

class ListReportsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Name of report, otherwise all reports by criteria",
      "order": 1
    },
    "sort": {
      "type": "string",
      "title": "Sort",
      "description": "Sort order, ascending or descending",
      "enum": [
        "Ascending",
        "Descending"
      ],
      "order": 2
    }
  },
  "required": [
    "sort"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListReportsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "Whether optional user supplied report name was found",
      "order": 1
    },
    "list": {
      "type": "array",
      "title": "List of Reports",
      "description": "List of report identifiers",
      "items": {
        "$ref": "#/definitions/report_id"
      },
      "order": 2
    }
  },
  "definitions": {
    "report_id": {
      "type": "object",
      "title": "report_id",
      "properties": {
        "id": {
          "type": "integer",
          "title": "Report ID",
          "description": "Identifer",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Report Name",
          "description": "Name of report",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
