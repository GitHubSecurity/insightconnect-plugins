# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    FIELDS = "fields"
    INCLUDE_EXPIRED = "include_expired"
    LIMIT = "limit"
    MAX_CONFIDENCE = "max_confidence"
    MIN_CONFIDENCE = "min_confidence"
    OWNER = "owner"
    REVIEW_STATUS = "review_status"
    SHARE_LEVEL = "share_level"
    SINCE = "since"
    SORT_BY = "sort_by"
    SORT_ORDER = "sort_order"
    STATUS = "status"
    STRICT_TEXT = "strict_text"
    TAGS = "tags"
    TEXT = "text"
    TYPE = "type"
    UNTIL = "until"
    

class Output:
    DATA = "data"
    PAGING = "paging"
    

class ThreatDescriptorsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "fields": {
      "type": "array",
      "title": "Fields",
      "description": "A list of fields to return in the response",
      "items": {
        "type": "string"
      },
      "order": 17
    },
    "include_expired": {
      "type": "boolean",
      "title": "Include Expired",
      "description": "When set to true, the API can return data which has expired",
      "default": false,
      "order": 1
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "description": "Defines the maximum size of a page of result",
      "order": 2
    },
    "max_confidence": {
      "type": "integer",
      "title": "Max Confidence",
      "description": "Define the maximum allowed confidence value for the data returned, range 0 - 100",
      "default": 100,
      "order": 3
    },
    "min_confidence": {
      "type": "integer",
      "title": "Minimum Confidence",
      "description": "Define the minimum allowed confidence value for the data returned, range 0 - 100",
      "default": 0,
      "order": 4
    },
    "owner": {
      "type": "array",
      "title": "Owner",
      "description": "Comma separated list of AppIDs of the person who submitted the data",
      "items": {
        "type": "string"
      },
      "order": 5
    },
    "review_status": {
      "type": "string",
      "title": "Review Status",
      "description": "A given ReviewStatusType",
      "enum": [
        "",
        "UNKNOWN",
        "UNREVIEWED",
        "PENDING",
        "REVIEWED_MANUALLY",
        "REVIEWED_AUTOMATICALLY"
      ],
      "order": 7
    },
    "share_level": {
      "type": "string",
      "title": "Share Level",
      "description": "The following Share Level Type designations are based on the US-CERT's Traffic Light Protocol and govern how ThreatData may be re-shared both within and outside of ThreatExchange",
      "enum": [
        "",
        "RED",
        "AMBER",
        "GREEN",
        "WHITE"
      ],
      "order": 8
    },
    "since": {
      "type": "string",
      "title": "Since",
      "description": "Returns descriptors collected after a timestamp",
      "order": 15
    },
    "sort_by": {
      "type": "string",
      "title": "Sort By",
      "description": "Sort search results by RELEVANCE or by CREATE_TIME. When sorting by RELEVANCE, your query will return results sorted by similarity against your text query",
      "enum": [
        "",
        "RELEVANCE",
        "CREATE_TIME"
      ],
      "order": 10
    },
    "sort_order": {
      "type": "string",
      "title": "Sort Order",
      "description": "An ordering with which to sort ThreatExchange results",
      "enum": [
        "",
        "ASCENDING",
        "DESCENDING"
      ],
      "order": 9
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "A description of the maliciousness of any object within ThreatExchange",
      "enum": [
        "",
        "UNKNOWN",
        "NON_MALICIOUS",
        "SUSPICIOUS",
        "MALICIOUS"
      ],
      "order": 11
    },
    "strict_text": {
      "type": "boolean",
      "title": "Strict Text",
      "description": "When set to 'true', the API will not do approximate matching on the value in text",
      "order": 12
    },
    "tags": {
      "type": "array",
      "title": "Tags",
      "description": "Comma separated list of tags to filter results",
      "items": {
        "type": "string"
      },
      "order": 13
    },
    "text": {
      "type": "string",
      "title": "Text",
      "description": "Freeform text field with a value to search for. This can be a file hash or a string found in other fields of the objects",
      "order": 6
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "The type of descriptor to search for",
      "enum": [
        "",
        "ADJUST_TOKEN",
        "API_KEY",
        "AS_NUMBER",
        "BANNER",
        "CMD_LINE",
        "COOKIE_NAME",
        "CRX",
        "DEBUG_STRING",
        "DEST_PORT",
        "DIRECTORY_QUERIED",
        "DOMAIN",
        "EMAIL_ADDRESS",
        "FILE_CREATED",
        "FILE_DELETED",
        "FILE_MOVED",
        "FILE_NAME",
        "FILE_OPENED",
        "FILE_READ",
        "FILE_WRITTEN",
        "GET_PARAM",
        "HASH_IMPHASH",
        "HASH_MD5",
        "HASH_SHA1",
        "HASH_SHA256",
        "HASH_SSDEEP",
        "HTML_ID",
        "HTTP_REQUEST",
        "IP_ADDRESS",
        "IP_SUBNET",
        "ISP",
        "LATITUDE",
        "LAUNCH_AGENT",
        "LOCATION",
        "LONGITUDE",
        "MALWARE_NAME",
        "MEMORY_ALLOC",
        "MEMORY_PROTECT",
        "MEMORY_WRITTEN",
        "MUTANT_CREATED",
        "MUTEX",
        "NAME_SERVER",
        "OTHER_FILE_OP",
        "PASSWORD",
        "PASSWORD_SALT",
        "PAYLOAD_DATA",
        "PAYLOAD_TYPE",
        "POST_DATA",
        "PROTOCOL",
        "REFERER",
        "REGISTRAR",
        "REGISTRY_KEY",
        "REG_KEY_CREATED",
        "REG_KEY_DELETED",
        "REG_KEY_ENUMERATED",
        "REG_KEY_MONITORED",
        "REG_KEY_OPENED",
        "REG_KEY_VALUE_CREATED",
        "REG_KEY_VALUE_DELETED",
        "REG_KEY_VALUE_MODIFIED",
        "REG_KEY_VALUE_QUERIED",
        "SIGNATURE",
        "SOURCE_PORT",
        "TELEPHONE",
        "URI",
        "USER_AGENT",
        "VOLUME_QUERIED",
        "WEBSTORAGE_KEY",
        "WEB_PAYLOAD",
        "WHOIS_NAME",
        "WHOIS_ADDR1",
        "WHOIS_ADDR2",
        "XPI"
      ],
      "order": 14
    },
    "until": {
      "type": "string",
      "title": "Until",
      "description": "Returns descriptors collected before a timestamp ",
      "order": 16
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ThreatDescriptorsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "array",
      "title": "Data",
      "description": "Information around the indicator such as the Indicator, Type and ID",
      "items": {
        "$ref": "#/definitions/descriptor_data"
      },
      "order": 1
    },
    "paging": {
      "$ref": "#/definitions/paging",
      "title": "Paging",
      "description": "Paging Information",
      "order": 2
    }
  },
  "required": [
    "data",
    "paging"
  ],
  "definitions": {
    "cursors": {
      "type": "object",
      "title": "cursors",
      "properties": {
        "after": {
          "type": "string",
          "title": "After",
          "description": "End of page",
          "order": 1
        },
        "before": {
          "type": "string",
          "title": "Before",
          "description": "Start of page",
          "order": 2
        }
      }
    },
    "descriptor_data": {
      "type": "object",
      "title": "descriptor_data",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "order": 6
        },
        "id": {
          "type": "string",
          "title": "Descriptor ID",
          "order": 1
        },
        "indicator": {
          "$ref": "#/definitions/indicator",
          "title": "Indicator",
          "order": 2
        },
        "owner": {
          "$ref": "#/definitions/owner",
          "title": "Owner",
          "order": 3
        },
        "raw_indicator": {
          "type": "string",
          "title": "Raw Indicator",
          "order": 5
        },
        "status": {
          "type": "string",
          "title": "Status",
          "order": 7
        },
        "type": {
          "type": "string",
          "title": "Type",
          "order": 4
        }
      },
      "definitions": {
        "indicator": {
          "type": "object",
          "title": "indicator",
          "properties": {
            "id": {
              "type": "string",
              "title": "ID",
              "order": 3
            },
            "indicator": {
              "type": "string",
              "title": "Indicator",
              "order": 1
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 2
            }
          }
        },
        "owner": {
          "type": "object",
          "title": "owner",
          "properties": {
            "email": {
              "type": "string",
              "title": "Email",
              "order": 2
            },
            "id": {
              "type": "string",
              "title": "ID",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 3
            }
          }
        }
      }
    },
    "indicator": {
      "type": "object",
      "title": "indicator",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "order": 3
        },
        "indicator": {
          "type": "string",
          "title": "Indicator",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "order": 2
        }
      }
    },
    "owner": {
      "type": "object",
      "title": "owner",
      "properties": {
        "email": {
          "type": "string",
          "title": "Email",
          "order": 2
        },
        "id": {
          "type": "string",
          "title": "ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 3
        }
      }
    },
    "paging": {
      "type": "object",
      "title": "paging",
      "properties": {
        "cursors": {
          "$ref": "#/definitions/cursors",
          "title": "Cursor",
          "description": "Start and end of the page",
          "order": 1
        },
        "next": {
          "type": "string",
          "title": "Next Result",
          "description": "Next result",
          "order": 2
        }
      },
      "definitions": {
        "cursors": {
          "type": "object",
          "title": "cursors",
          "properties": {
            "after": {
              "type": "string",
              "title": "After",
              "description": "End of page",
              "order": 1
            },
            "before": {
              "type": "string",
              "title": "Before",
              "description": "Start of page",
              "order": 2
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
