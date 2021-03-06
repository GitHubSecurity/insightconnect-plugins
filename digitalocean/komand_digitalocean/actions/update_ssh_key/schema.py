# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    NAME = "name"
    SSH_KEY_ID = "ssh_key_id"
    

class Output:
    SSH_KEY = "ssh_key"
    

class UpdateSshKeyInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "name": {
      "type": "string",
      "title": "SSH Key Name",
      "description": "New name for the SSH key",
      "order": 2
    },
    "ssh_key_id": {
      "type": "string",
      "title": "SSH Key ID",
      "description": "SSH Key ID",
      "order": 1
    }
  },
  "required": [
    "ssh_key_id",
    "name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateSshKeyOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ssh_key": {
      "$ref": "#/definitions/ssh_key",
      "title": "Updated SSH Key",
      "description": "Updated SSH Key",
      "order": 1
    }
  },
  "definitions": {
    "ssh_key": {
      "type": "object",
      "title": "ssh_key",
      "properties": {
        "fingerprint": {
          "type": "string",
          "title": "Fingerprint",
          "order": 2
        },
        "id": {
          "type": "integer",
          "title": "Id",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 4
        },
        "public_key": {
          "type": "string",
          "title": "Public Key",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
