# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    
    AFTER = "after"
    INCLUDE_CVRF = "include_cvrf"
    

class Output:
    
    BUGZILLAS = "bugzillas"
    CVES = "cves"
    NOTES = "notes"
    OVAL = "oval"
    PUBLISHER = "publisher"
    REFERENCES = "references"
    RELEASED_ON = "released_on"
    RELEASED_PACKAGES = "released_packages"
    RESOURCE_URL = "resource_url"
    RHSA = "rhsa"
    SEVERITY = "severity"
    SOURCE = "source"
    TITLE = "title"
    TYPE = "type"
    URL = "url"
    

class NewAdvisoryInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "after": {
      "type": "string",
      "title": "After",
      "description": "Look for new advisories after provided date. Default is when trigger starts",
      "order": 1
    },
    "include_cvrf": {
      "type": "boolean",
      "title": "Include Cvrf",
      "description": "Include the full source CVRF",
      "default": false,
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class NewAdvisoryOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "bugzillas": {
      "type": "array",
      "title": "Bugzilla IDs",
      "description": "Bugzilla IDs",
      "items": {
        "type": "string"
      },
      "order": 11
    },
    "cves": {
      "type": "array",
      "title": "CVEs",
      "description": "CVE IDs",
      "items": {
        "type": "string"
      },
      "order": 10
    },
    "notes": {
      "type": "string",
      "title": "Notes",
      "description": "Notes",
      "order": 4
    },
    "oval": {
      "type": "object",
      "title": "Oval",
      "description": "OVAL",
      "order": 13
    },
    "publisher": {
      "$ref": "#/definitions/publisher",
      "title": "Publisher",
      "description": "Publisher",
      "order": 6
    },
    "references": {
      "type": "array",
      "title": "References",
      "description": "URL references",
      "items": {
        "$ref": "#/definitions/reference"
      },
      "order": 7
    },
    "released_on": {
      "type": "string",
      "title": "Released On",
      "displayType": "date",
      "description": "Release Date",
      "format": "date-time",
      "order": 9
    },
    "released_packages": {
      "type": "array",
      "title": "Released Packages",
      "description": "Released Packages",
      "items": {
        "type": "string"
      },
      "order": 12
    },
    "resource_url": {
      "type": "string",
      "title": "Resource Url",
      "description": "Resource JSON URL",
      "order": 14
    },
    "rhsa": {
      "type": "string",
      "title": "Rhsa",
      "description": "Red Hat Security Advisory ID",
      "order": 1
    },
    "severity": {
      "type": "string",
      "title": "Severity",
      "description": "Severity",
      "order": 8
    },
    "source": {
      "type": "object",
      "title": "Source",
      "description": "Original Source CVRF doc",
      "order": 15
    },
    "title": {
      "type": "string",
      "title": "Title",
      "description": "Title of Advisory",
      "order": 2
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "Type, e.g. 'Security Advisory'",
      "order": 5
    },
    "url": {
      "type": "string",
      "title": "Url",
      "description": "URL to advisory",
      "order": 3
    }
  },
  "definitions": {
    "publisher": {
      "type": "object",
      "title": "publisher",
      "properties": {
        "contact_details": {
          "type": "string",
          "title": "Contact Details",
          "description": "Who to contact",
          "order": 3
        },
        "issuing_authority": {
          "type": "string",
          "title": "Issuing Authority",
          "description": "Issuer",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type of Publisher",
          "order": 2
        }
      }
    },
    "reference": {
      "type": "object",
      "title": "reference",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Reference Description",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Ref Type (e.g. Self)",
          "order": 3
        },
        "url": {
          "type": "string",
          "title": "Url",
          "description": "URL",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
