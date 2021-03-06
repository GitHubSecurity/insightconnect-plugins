# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    DATE = "date"
    

class Output:
    ERROR = "error"
    STATS = "stats"
    

class ManagerStatsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "date": {
      "type": "string",
      "title": "Date",
      "description": "Selects the date for getting the statistical information. Format: YYYYMMDD",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ManagerStatsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "error": {
      "type": "integer",
      "title": "Error Code",
      "description": "Error code",
      "order": 2
    },
    "stats": {
      "type": "array",
      "title": "Stats",
      "description": "Stats",
      "items": {
        "$ref": "#/definitions/stats"
      },
      "order": 1
    }
  },
  "required": [
    "stats",
    "error"
  ],
  "definitions": {
    "alerts": {
      "type": "object",
      "title": "alerts",
      "properties": {
        "level": {
          "type": "integer",
          "title": "Level",
          "description": "Level",
          "order": 1
        },
        "sigid": {
          "type": "integer",
          "title": "Signature ID",
          "description": "Signature ID",
          "order": 2
        },
        "times": {
          "type": "integer",
          "title": "Times",
          "description": "Time",
          "order": 3
        }
      }
    },
    "stats": {
      "type": "object",
      "title": "stats",
      "properties": {
        "alerts": {
          "type": "array",
          "title": "Alerts",
          "description": "Alerts",
          "items": {
            "$ref": "#/definitions/alerts"
          },
          "order": 1
        },
        "events": {
          "type": "integer",
          "title": "Events",
          "description": "Events",
          "order": 2
        },
        "firewall": {
          "type": "integer",
          "title": "Firewall",
          "description": "Firewall",
          "order": 3
        },
        "hour": {
          "type": "integer",
          "title": "Hour",
          "description": "Hour",
          "order": 4
        },
        "syscheck": {
          "type": "integer",
          "title": "SysCheck",
          "description": "Syscheck",
          "order": 5
        },
        "totalAlerts": {
          "type": "integer",
          "title": "Total Alerts",
          "description": "Total Alerts",
          "order": 6
        }
      },
      "definitions": {
        "alerts": {
          "type": "object",
          "title": "alerts",
          "properties": {
            "level": {
              "type": "integer",
              "title": "Level",
              "description": "Level",
              "order": 1
            },
            "sigid": {
              "type": "integer",
              "title": "Signature ID",
              "description": "Signature ID",
              "order": 2
            },
            "times": {
              "type": "integer",
              "title": "Times",
              "description": "Time",
              "order": 3
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
