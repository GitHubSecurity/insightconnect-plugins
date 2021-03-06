# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    CERTIFICATE = "certificate"
    FORMAT = "format"
    HSM = "hsm"
    PKCS12FILE = "pkcs12file"
    PKCS12PASSWORD = "pkcs12password"
    PRIVATE = "private"
    SERVERGROUPNAME = "servergroupname"
    SITENAME = "sitename"
    SSLKEYNAME = "sslkeyname"
    WEBSERVICENAME = "webservicename"
    

class Output:
    STATUS_CODE = "status_code"
    

class UploadSslCertificateInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "certificate": {
      "type": "string",
      "title": "Certificate",
      "displayType": "bytes",
      "description": "Base64 encoded PEM certificate, enclosed between '-----BEGIN CERTIFICATE-----' and '-----END CERTIFICATE-----'",
      "format": "bytes",
      "order": 7
    },
    "format": {
      "type": "string",
      "title": "Format",
      "description": "Certificate format type",
      "enum": [
        "pem",
        "pkcs12"
      ],
      "order": 5
    },
    "hsm": {
      "type": "boolean",
      "title": "HSM",
      "description": "Is certificate used by HSM",
      "default": false,
      "order": 8
    },
    "pkcs12file": {
      "type": "string",
      "title": "PKCS12 File",
      "displayType": "bytes",
      "description": "PKCS12 file content",
      "format": "bytes",
      "order": 9
    },
    "pkcs12password": {
      "type": "string",
      "title": "PKCS12 Password",
      "displayType": "password",
      "description": "PKCS12 file password",
      "format": "password",
      "order": 10
    },
    "private": {
      "type": "string",
      "title": "Private",
      "displayType": "bytes",
      "description": "Base64 encoded PEM certificate, enclosed between '-----BEGIN PRIVATE-----' and '----- END PRIVATE-----'",
      "format": "bytes",
      "order": 6
    },
    "servergroupname": {
      "type": "string",
      "title": "Server Group Name",
      "description": "The name of the parent server group of the web service to access",
      "order": 2
    },
    "sitename": {
      "type": "string",
      "title": "Site Name",
      "description": "The name of the parent site of the web service to access",
      "order": 1
    },
    "sslkeyname": {
      "type": "string",
      "title": "SSL Key Name",
      "description": "The name of the SSL Key to create",
      "order": 4
    },
    "webservicename": {
      "type": "string",
      "title": "Web Service Name",
      "description": "The name of the web service to access",
      "order": 3
    }
  },
  "required": [
    "servergroupname",
    "webservicename",
    "sitename",
    "sslkeyname",
    "format"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UploadSslCertificateOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status_code": {
      "type": "integer",
      "title": "Status Code",
      "description": "HTTP status code",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
