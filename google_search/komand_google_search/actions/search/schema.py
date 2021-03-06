# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    LANG = "lang"
    NUM = "num"
    ONLY_STANDARD = "only_standard"
    PAUSE = "pause"
    QUERY = "query"
    STOP = "stop"
    

class Output:
    URLS = "urls"
    

class SearchInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "lang": {
      "type": "string",
      "title": "Language",
      "description": "Language, default is en",
      "default": "en",
      "order": 2
    },
    "num": {
      "type": "integer",
      "title": "Number",
      "description": "Number of results per page, default is 10",
      "default": 10,
      "order": 4
    },
    "only_standard": {
      "type": "boolean",
      "title": "All",
      "description": "Only returns the standard results from each page. If false, it returns every possible link from each page, except for those that point back to Google itself",
      "default": false,
      "order": 5
    },
    "pause": {
      "type": "number",
      "title": "Pause",
      "description": "Lapse to wait between HTTP requests. A lapse too long will make the search slow, but a lapse too short may cause Google to block your IP. Your mileage may vary",
      "default": 1,
      "order": 6
    },
    "query": {
      "type": "string",
      "title": "Query",
      "description": "Query string. Must NOT be URL-encoded",
      "order": 1
    },
    "stop": {
      "type": "integer",
      "title": "Stop",
      "description": "Number of results to retrieve to limit amount, default is 16 and the search will allows return at least 16 results if available. This option seems to have odd behavior",
      "default": 16,
      "order": 3
    }
  },
  "required": [
    "query",
    "lang",
    "stop",
    "num",
    "only_standard",
    "pause"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "urls": {
      "type": "array",
      "title": "URLs",
      "description": "List of URLs",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  },
  "required": [
    "urls"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
