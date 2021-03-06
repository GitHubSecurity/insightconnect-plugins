# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ID = "id"
    PARAMETERS = "parameters"
    

class Output:
    ASSIGNEE = "assignee"
    ASSIGNEES = "assignees"
    AUTHOR = "author"
    CONFIDENTIAL = "confidential"
    CREATED_AT = "created_at"
    DESCRIPTION = "description"
    DUE_DATE = "due_date"
    ID = "id"
    IID = "iid"
    LABELS = "labels"
    MILESTONE = "milestone"
    PROJECT_ID = "project_id"
    STATE = "state"
    SUBSCRIBED = "subscribed"
    TITLE = "title"
    UPDATED_AT = "updated_at"
    USER_NOTES_COUNT = "user_notes_count"
    WEB_URL = "web_url"
    

class CreateIssueInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "User ID",
      "description": "User ID to unblock",
      "order": 1
    },
    "parameters": {
      "$ref": "#/definitions/issue_input",
      "title": "Issue Parameters",
      "description": "Issue parameters",
      "order": 2
    }
  },
  "required": [
    "id"
  ],
  "definitions": {
    "issue_input": {
      "type": "object",
      "title": "issue_input",
      "properties": {
        "assignee_ids": {
          "type": "array",
          "title": "Assignees",
          "description": "The ID of a user to assign issue",
          "items": {
            "type": "integer"
          },
          "order": 5
        },
        "confidential": {
          "type": "boolean",
          "title": "Confidential",
          "description": "Set an issue to be confidential",
          "order": 4
        },
        "created_at": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "description": "Date, ISO 8601 formatted (requires admin or project owner rights)",
          "format": "date-time",
          "order": 8
        },
        "description": {
          "type": "string",
          "title": "Description title",
          "description": "The description of an issue",
          "order": 3
        },
        "discussion_resolve": {
          "type": "string",
          "title": "Discussion To Resolve",
          "description": "The ID of a discussion to resolve",
          "order": 11
        },
        "due_date": {
          "type": "string",
          "title": "Due Date",
          "displayType": "date",
          "description": "Date time string in the format YEAR-MONTH-DAY",
          "format": "date-time",
          "order": 9
        },
        "labels": {
          "type": "string",
          "title": "Labels",
          "description": "Comma-separated label names for an issue",
          "order": 7
        },
        "merge_request": {
          "type": "integer",
          "title": "Merge Request To Resolve Discussions Of",
          "description": "The IID of a merge request in which to resolve all issues",
          "order": 10
        },
        "milestone_id": {
          "type": "integer",
          "title": "Milestone",
          "description": "The ID of a milestone to assign issue",
          "order": 6
        },
        "project_id": {
          "type": "integer",
          "title": "Project ID",
          "description": "ID of project",
          "order": 1
        },
        "title": {
          "type": "string",
          "title": "Issue title",
          "description": "The title of an issue",
          "order": 2
        }
      },
      "required": [
        "title",
        "project_id"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateIssueOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "assignee": {
      "$ref": "#/definitions/user_output",
      "title": "Assignee",
      "description": "Assignee",
      "order": 8
    },
    "assignees": {
      "type": "array",
      "title": "Assignees",
      "description": "Assignees",
      "items": {
        "$ref": "#/definitions/user_output"
      },
      "order": 7
    },
    "author": {
      "$ref": "#/definitions/user_output",
      "title": "Author",
      "description": "Author",
      "order": 18
    },
    "confidential": {
      "type": "boolean",
      "title": "Confidential",
      "description": "Confidential",
      "order": 17
    },
    "created_at": {
      "type": "string",
      "title": "Created At",
      "displayType": "date",
      "description": "Created at",
      "format": "date-time",
      "order": 3
    },
    "description": {
      "type": "string",
      "title": "Description",
      "description": "Description",
      "order": 10
    },
    "due_date": {
      "type": "string",
      "title": "Due Date",
      "displayType": "date",
      "description": "Due date",
      "format": "date-time",
      "order": 15
    },
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "ID",
      "order": 2
    },
    "iid": {
      "type": "integer",
      "title": "IID",
      "description": "IID",
      "order": 4
    },
    "labels": {
      "type": "array",
      "title": "Labels",
      "description": "Labels",
      "items": {
        "type": "string"
      },
      "order": 9
    },
    "milestone": {
      "$ref": "#/definitions/milestone_output",
      "title": "Milestone",
      "description": "Milestone",
      "order": 12
    },
    "project_id": {
      "type": "integer",
      "title": "Project ID",
      "description": "Project ID",
      "order": 1
    },
    "state": {
      "type": "string",
      "title": "State",
      "description": "State",
      "order": 6
    },
    "subscribed": {
      "type": "boolean",
      "title": "Subscribed",
      "description": "Subscribed",
      "order": 13
    },
    "title": {
      "type": "string",
      "title": "Title",
      "description": "Title",
      "order": 5
    },
    "updated_at": {
      "type": "string",
      "title": "Updated At",
      "displayType": "date",
      "description": "Updated at",
      "format": "date-time",
      "order": 11
    },
    "user_notes_count": {
      "type": "integer",
      "title": "User Notes Count",
      "description": "User notes count",
      "order": 14
    },
    "web_url": {
      "type": "string",
      "title": "Web URL",
      "description": "Web URL",
      "order": 16
    }
  },
  "definitions": {
    "milestone_output": {
      "type": "object",
      "title": "milestone_output",
      "properties": {
        "created_at": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "description": "Date project was created",
          "format": "date-time",
          "order": 7
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Project Description",
          "order": 5
        },
        "due_date": {
          "type": "string",
          "title": "Due Date",
          "displayType": "date",
          "description": "Date project is to be closed",
          "format": "date-time",
          "order": 9
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Unique milestone ID",
          "order": 1
        },
        "iid": {
          "type": "integer",
          "title": "IID",
          "description": "Unique ID only in scope of a single project",
          "order": 2
        },
        "project_id": {
          "type": "integer",
          "title": "Project ID",
          "description": "Project ID",
          "order": 3
        },
        "state": {
          "type": "string",
          "title": "State",
          "description": "Project State e.g. 'Opened', 'Closed'",
          "order": 6
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Project title",
          "order": 4
        },
        "updated_at": {
          "type": "string",
          "title": "Updated At",
          "displayType": "date",
          "description": "Date project was updated",
          "format": "date-time",
          "order": 8
        }
      }
    },
    "user_output": {
      "type": "object",
      "title": "user_output",
      "properties": {
        "avatar_url": {
          "type": "string",
          "title": "Avatar URL",
          "description": "User avatar URL",
          "order": 2
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Unique user ID",
          "order": 5
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "User full name",
          "order": 1
        },
        "state": {
          "type": "string",
          "title": "State",
          "description": "User state 'Active' or 'Inactive' ",
          "order": 3
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "User's username",
          "order": 6
        },
        "web_url": {
          "type": "string",
          "title": "Web URL",
          "description": "User profile URL",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
