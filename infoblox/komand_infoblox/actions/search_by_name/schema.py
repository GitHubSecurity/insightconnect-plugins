# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    NAME_PATTERN = "name_pattern"
    

class Output:
    RESULT = "result"
    

class SearchByNameInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "name_pattern": {
      "type": "string",
      "title": "Name Pattern",
      "description": "Regular expression to match against host name",
      "order": 1
    }
  },
  "required": [
    "name_pattern"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchByNameOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "result": {
      "type": "array",
      "title": "Result",
      "description": "Matched hosts",
      "items": {
        "$ref": "#/definitions/Host"
      },
      "order": 1
    }
  },
  "required": [
    "result"
  ],
  "definitions": {
    "Host": {
      "type": "object",
      "title": "Host",
      "properties": {
        "_ref": {
          "type": "string",
          "title": "Ref",
          "description": "Object Reference of the host",
          "order": 1
        },
        "aliases": {
          "type": "array",
          "title": "Aliases",
          "description": "Aliases associated with the host",
          "items": {
            "type": "string"
          },
          "order": 6
        },
        "extattrs": {
          "type": "object",
          "title": "Extattrs",
          "description": "Extensible attributes",
          "order": 5
        },
        "ipv4addrs": {
          "type": "array",
          "title": "IPv4 Addresses",
          "description": "IP addresses associated with the new host",
          "items": {
            "$ref": "#/definitions/IPv4Addr"
          },
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the new host",
          "order": 2
        },
        "view": {
          "type": "string",
          "title": "View",
          "description": "The network view this host is associated with",
          "order": 4
        }
      },
      "required": [
        "_ref",
        "name",
        "ipv4addrs"
      ],
      "definitions": {
        "IPv4Addr": {
          "type": "object",
          "title": "IPv4Addr",
          "properties": {
            "_ref": {
              "type": "string",
              "title": "Ref",
              "description": "Object Reference of the IP address",
              "order": 5
            },
            "configure_for_dhcp": {
              "type": "boolean",
              "title": "Configure for DHCP",
              "description": "Configure for DHCP flag",
              "order": 3
            },
            "host": {
              "type": "string",
              "title": "Host",
              "description": "The name of the host",
              "order": 4
            },
            "ipv4addr": {
              "type": "string",
              "title": "IPv4 Address",
              "description": "Either an IP address or a function (e.g. func:nextavailableip:10.1.1.0/24)",
              "order": 1
            },
            "mac": {
              "type": "string",
              "title": "MAC",
              "description": "MAC address",
              "order": 2
            }
          },
          "required": [
            "_ref",
            "ipv4addr"
          ]
        }
      }
    },
    "IPv4Addr": {
      "type": "object",
      "title": "IPv4Addr",
      "properties": {
        "_ref": {
          "type": "string",
          "title": "Ref",
          "description": "Object Reference of the IP address",
          "order": 5
        },
        "configure_for_dhcp": {
          "type": "boolean",
          "title": "Configure for DHCP",
          "description": "Configure for DHCP flag",
          "order": 3
        },
        "host": {
          "type": "string",
          "title": "Host",
          "description": "The name of the host",
          "order": 4
        },
        "ipv4addr": {
          "type": "string",
          "title": "IPv4 Address",
          "description": "Either an IP address or a function (e.g. func:nextavailableip:10.1.1.0/24)",
          "order": 1
        },
        "mac": {
          "type": "string",
          "title": "MAC",
          "description": "MAC address",
          "order": 2
        }
      },
      "required": [
        "_ref",
        "ipv4addr"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
