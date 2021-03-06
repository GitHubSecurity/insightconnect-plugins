# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Approve file locally"


class Input:
    FILE_ID = "file_id"
    

class Output:
    FILE_INSTANCE = "file_instance"
    

class ApproveFileLocallyInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file_id": {
      "type": "integer",
      "title": "File ID",
      "description": "File ID of file to approve locally",
      "order": 1
    }
  },
  "required": [
    "file_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ApproveFileLocallyOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file_instance": {
      "$ref": "#/definitions/fileInstance",
      "title": "File Instance",
      "description": "Updated file instance",
      "order": 1
    }
  },
  "definitions": {
    "fileInstance": {
      "type": "object",
      "title": "fileInstance",
      "properties": {
        "computerId": {
          "type": "integer",
          "title": "Computer ID",
          "order": 4
        },
        "dateCreated": {
          "type": "string",
          "title": "Date Created",
          "displayType": "date",
          "description": "Datetime when File Was Created (UTC)",
          "format": "date-time",
          "order": 5
        },
        "detachedCertificateId": {
          "type": "integer",
          "title": "Detached CertificateId",
          "description": "Id of Detached Certificate That Signed This File through the Catalog",
          "order": 12
        },
        "detachedPublisherId": {
          "type": "integer",
          "title": "Detached Publisher ID",
          "description": "Id of Detached Publisher That Signed This File through the Catalog",
          "order": 11
        },
        "detailedLocalState": {
          "type": "integer",
          "title": "Detailed Local State",
          "order": 10
        },
        "executed": {
          "type": "boolean",
          "title": "Executed",
          "description": "True if File Was Ever Executed on Agent",
          "order": 8
        },
        "fileCatalogId": {
          "type": "integer",
          "title": "File Catalog ID",
          "order": 2
        },
        "fileInstanceGroupId": {
          "type": "integer",
          "title": "File Instance Group ID",
          "order": 3
        },
        "fileName": {
          "type": "string",
          "title": "File Name",
          "order": 6
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "order": 1
        },
        "localState": {
          "type": "integer",
          "title": "Local State",
          "order": 9
        },
        "pathName": {
          "type": "string",
          "title": "Path Name",
          "order": 7
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
