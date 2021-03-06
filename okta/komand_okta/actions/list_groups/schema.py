# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    QUERY = "query"
    

class Output:
    GROUPS = "groups"
    SUCCESS = "success"
    

class ListGroupsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "query": {
      "type": "string",
      "title": "Query",
      "description": "Query to list groups, otherwise all groups will be returned",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListGroupsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "groups": {
      "type": "array",
      "title": "Groups",
      "description": "List of groups",
      "items": {
        "$ref": "#/definitions/group"
      },
      "order": 2
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether groups were found",
      "order": 1
    }
  },
  "required": [
    "success"
  ],
  "definitions": {
    "group": {
      "type": "object",
      "title": "group",
      "properties": {
        "created": {
          "type": "string",
          "title": "Created",
          "description": "Created",
          "order": 2
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Group ID",
          "order": 7
        },
        "lastMembershipUpdated": {
          "type": "string",
          "title": "Last Membership Updated",
          "description": "Last membership updated",
          "order": 5
        },
        "lastUpdated": {
          "type": "string",
          "title": "Last Updated",
          "description": "Last updated",
          "order": 4
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Group name",
          "order": 1
        },
        "objectClass": {
          "type": "array",
          "title": "Object Class",
          "description": "Object class",
          "items": {
            "type": "string"
          },
          "order": 3
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 6
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
