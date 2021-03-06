# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    CONSISTENCY = "consistency"
    DATA = "data"
    DATABASE_NAME = "database_name"
    PASSWORD = "password"
    PRECISION = "precision"
    RETENTION_POLICY = "retention_policy"
    USERNAME = "username"
    

class Output:
    MESSAGE = "message"
    STATUS_CODE = "status_code"
    

class WriteInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "consistency": {
      "type": "string",
      "title": "Consistency",
      "description": "Sets the write consistency for the point. One of [any,one,quorum,all]",
      "enum": [
        "any",
        "one",
        "quorum",
        "all"
      ],
      "order": 2
    },
    "data": {
      "type": "string",
      "title": "Data",
      "description": "Data to be written into the database. Must be in Line Protocol format. See https://docs.influxdata.com/influxdb/v1.2/write_protocols/line_protocol_tutorial/",
      "order": 7
    },
    "database_name": {
      "type": "string",
      "title": "Database",
      "description": "Database name",
      "order": 1
    },
    "password": {
      "type": "string",
      "title": "Password",
      "displayType": "password",
      "description": "Set the password for authentication",
      "format": "password",
      "order": 6
    },
    "precision": {
      "type": "string",
      "title": "Precision",
      "description": "Sets the precision for the supplied Unix time values",
      "order": 3
    },
    "retention_policy": {
      "type": "string",
      "title": "Retention Policy",
      "description": "Sets the target retention policy for the write",
      "order": 4
    },
    "username": {
      "type": "string",
      "title": "Username",
      "description": "Sets the username for authentication",
      "order": 5
    }
  },
  "required": [
    "database_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class WriteOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Message",
      "order": 2
    },
    "status_code": {
      "type": "integer",
      "title": "Status Code",
      "description": "Status code",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
