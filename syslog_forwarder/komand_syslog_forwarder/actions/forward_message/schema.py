# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    FACILITY = "facility"
    HOST = "host"
    LEVEL = "level"
    MSG = "msg"
    MSGID = "msgid"
    PROC = "proc"
    

class Output:
    pass

class ForwardMessageInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "facility": {
      "type": "string",
      "title": "Facility",
      "description": "Syslog Facility",
      "enum": [
        "KERN",
        "USER",
        "MAIL",
        "DAEMON",
        "AUTH",
        "SYSLOG",
        "LPR",
        "NEWS",
        "UUCP",
        "CRON",
        "AUTHPRIV",
        "FTP",
        "LOCAL0",
        "LOCAL1",
        "LOCAL2",
        "LOCAL3",
        "LOCAL4",
        "LOCAL5",
        "LOCAL6",
        "LOCAL7"
      ],
      "order": 2
    },
    "host": {
      "type": "string",
      "title": "Host",
      "description": "Name or address where message originated from",
      "order": 4
    },
    "level": {
      "type": "string",
      "title": "Level",
      "description": "Syslog Level",
      "enum": [
        "EMERG",
        "ALERT",
        "CRIT",
        "ERR",
        "WARNING",
        "NOTICE",
        "INFO",
        "DEBUG"
      ],
      "order": 3
    },
    "msg": {
      "type": "string",
      "title": "Message",
      "description": "Syslog message",
      "order": 1
    },
    "msgid": {
      "type": "string",
      "title": "Message ID",
      "description": "Message ID",
      "order": 5
    },
    "proc": {
      "type": "string",
      "title": "Process Name",
      "description": "Process name",
      "order": 6
    }
  },
  "required": [
    "facility",
    "level",
    "msg"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ForwardMessageOutput(komand.Output):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
