# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ARCHIVE = "archive"
    

class Output:
    FILES = "files"
    

class ExtractArchiveInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "archive": {
      "$ref": "#/definitions/file",
      "title": "Archive",
      "description": "Base64-encoded archive file",
      "order": 1
    }
  },
  "required": [
    "archive"
  ],
  "definitions": {
    "file": {
      "id": "file",
      "type": "object",
      "title": "File",
      "description": "File Object",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "description": "File contents",
          "format": "bytes"
        },
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of file"
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ExtractArchiveOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "files": {
      "type": "array",
      "title": "Files",
      "description": "Files",
      "items": {
        "$ref": "#/definitions/file"
      },
      "order": 1
    }
  },
  "definitions": {
    "file": {
      "id": "file",
      "type": "object",
      "title": "File",
      "description": "File Object",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "description": "File contents",
          "format": "bytes"
        },
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of file"
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
