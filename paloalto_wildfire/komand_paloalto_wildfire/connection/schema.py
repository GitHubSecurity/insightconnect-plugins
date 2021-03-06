# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    API_KEY = "api_key"
    HOST = "host"
    PROXY = "proxy"
    VERIFY = "verify"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Wildfire API Key",
      "description": "Wildfire API Key, available at https://wildfire.paloaltonetworks.com/wildfire/account or on your appliance",
      "order": 2
    },
    "host": {
      "type": "string",
      "title": "Host",
      "description": "Palo Alto Wildfire host in cloud or on-premise, e.g. wildfire.paloaltonetworks.com or 10.3.4.50",
      "default": "wildfire.paloaltonetworks.com",
      "order": 1
    },
    "proxy": {
      "type": "object",
      "title": "Proxy",
      "description": "An optional dictionary containing proxy data, with https as the key, and the proxy path as the value",
      "order": 3
    },
    "verify": {
      "type": "boolean",
      "title": "SSL Verify",
      "description": "Verify the certificate",
      "default": true,
      "order": 4
    }
  },
  "required": [
    "verify",
    "host",
    "api_key"
  ],
  "definitions": {
    "credential_secret_key": {
      "id": "credential_secret_key",
      "type": "object",
      "title": "Credential: Secret Key",
      "description": "A shared secret key",
      "properties": {
        "secretKey": {
          "type": "string",
          "title": "Secret Key",
          "displayType": "password",
          "description": "The shared secret key",
          "format": "password"
        }
      },
      "required": [
        "secretKey"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
