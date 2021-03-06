# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ISSUE_NUMBER = "issue_number"
    REPO_ID = "repo_id"
    

class Output:
    DATA = "data"
    

class GetIssueDataInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "issue_number": {
      "type": "integer",
      "title": "Issue Number",
      "description": "GitHub Issue Number",
      "order": 2
    },
    "repo_id": {
      "type": "integer",
      "title": "Repository ID",
      "description": "GitHub Repository ID e.g. 24237263",
      "order": 1
    }
  },
  "required": [
    "repo_id",
    "issue_number"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetIssueDataOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "$ref": "#/definitions/issue_data",
      "title": "Issue Data",
      "description": "ZenHub Issue Data",
      "order": 1
    }
  },
  "definitions": {
    "issue_data": {
      "type": "object",
      "title": "issue_data",
      "properties": {
        "estimate_value": {
          "type": "integer",
          "title": "Estimated Value",
          "description": "Estimated value",
          "order": 6
        },
        "is_epic": {
          "type": "boolean",
          "title": "Is epic",
          "description": "Is epic",
          "order": 3
        },
        "issue_number": {
          "type": "integer",
          "title": "Issue number",
          "description": "Issue number",
          "order": 1
        },
        "pipeline_name": {
          "type": "string",
          "title": "Pipelne Name",
          "description": "Pipeline name",
          "order": 5
        },
        "plus_ones": {
          "type": "array",
          "title": "Plus One",
          "description": "Plus one",
          "items": {
            "$ref": "#/definitions/plus_one"
          },
          "order": 7
        },
        "position": {
          "type": "integer",
          "title": "Position",
          "description": "Position",
          "order": 4
        },
        "repo_id": {
          "type": "integer",
          "title": "Repo id",
          "description": "Repo id",
          "order": 2
        }
      },
      "definitions": {
        "plus_one": {
          "type": "object",
          "title": "plus_one",
          "properties": {
            "created_at": {
              "type": "string",
              "title": "Created At",
              "displayType": "date",
              "description": "Created at",
              "format": "date-time",
              "order": 2
            },
            "user_id": {
              "type": "integer",
              "title": "User Id",
              "description": "User ID",
              "order": 1
            }
          }
        }
      }
    },
    "plus_one": {
      "type": "object",
      "title": "plus_one",
      "properties": {
        "created_at": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "description": "Created at",
          "format": "date-time",
          "order": 2
        },
        "user_id": {
          "type": "integer",
          "title": "User Id",
          "description": "User ID",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
