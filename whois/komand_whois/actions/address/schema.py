# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ADDRESS = "address"
    

class Output:
    ADDRESS = "address"
    CIDR = "cidr"
    CITY = "city"
    COUNTRY = "country"
    NETNAME = "netname"
    NETRANGE = "netrange"
    NETTYPE = "nettype"
    ORG_ABUSE_EMAIL = "org_abuse_email"
    ORG_ABUSE_PHONE = "org_abuse_phone"
    ORG_TECH_EMAIL = "org_tech_email"
    ORG_TECH_PHONE = "org_tech_phone"
    ORGANIZATION = "organization"
    ORGNAME = "orgname"
    POSTAL = "postal"
    REGDATE = "regdate"
    STATE = "state"
    UPDATE = "update"
    

class AddressInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "Address",
      "description": "IP to Lookup",
      "order": 1
    }
  },
  "required": [
    "address"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddressOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "Address",
      "description": "Address",
      "order": 9
    },
    "cidr": {
      "type": "string",
      "title": "CIDR",
      "description": "CIDR",
      "order": 4
    },
    "city": {
      "type": "string",
      "title": "City",
      "description": "City",
      "order": 10
    },
    "country": {
      "type": "string",
      "title": "Country",
      "description": "Country",
      "order": 13
    },
    "netname": {
      "type": "string",
      "title": "Network Name",
      "description": "Network name",
      "order": 1
    },
    "netrange": {
      "type": "string",
      "title": "Network Range",
      "description": "Network Range",
      "order": 3
    },
    "nettype": {
      "type": "string",
      "title": "Network Type",
      "description": "Network type",
      "order": 2
    },
    "org_abuse_email": {
      "type": "string",
      "title": "Organization Abuse E-mail",
      "description": "Organization abuse e-mail",
      "order": 14
    },
    "org_abuse_phone": {
      "type": "string",
      "title": "Organization Abuse Phone",
      "description": "Organization abuse phone",
      "order": 15
    },
    "org_tech_email": {
      "type": "string",
      "title": "Organization Tech E-mail",
      "description": "Organization tech e-mail",
      "order": 16
    },
    "org_tech_phone": {
      "type": "string",
      "title": "Organization Tech Phone",
      "description": "Organization tech phone",
      "order": 17
    },
    "organization": {
      "type": "string",
      "title": "Organization",
      "description": "Organization",
      "order": 5
    },
    "orgname": {
      "type": "string",
      "title": "Organization Name",
      "description": "Organization name",
      "order": 6
    },
    "postal": {
      "type": "string",
      "title": "Postal",
      "description": "Postal",
      "order": 11
    },
    "regdate": {
      "type": "string",
      "title": "Registration Date",
      "description": "Registration date",
      "order": 7
    },
    "state": {
      "type": "string",
      "title": "State",
      "description": "State",
      "order": 12
    },
    "update": {
      "type": "string",
      "title": "Whois Updated Date",
      "description": "Whois updated date",
      "order": 8
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
