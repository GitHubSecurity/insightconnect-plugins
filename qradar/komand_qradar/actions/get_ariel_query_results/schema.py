# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    SEARCH_ID = "search_id"
    

class Output:
    COMPRESSED_DATA_FILE_COUNT = "compressed_data_file_count"
    COMPRESSED_DATA_TOTAL_SIZE = "compressed_data_total_size"
    CURSOR_ID = "cursor_id"
    DATA_FILE_COUNT = "data_file_count"
    DATA_TOTAL_SIZE = "data_total_size"
    DESIRED_RETENTION_TIME_MSEC = "desired_retention_time_msec"
    ERROR_MESSAGES = "error_messages"
    INDEX_FILE_COUNT = "index_file_count"
    INDEX_TOTAL_SIZE = "index_total_size"
    PROCESSED_RECORD_COUNT = "processed_record_count"
    PROGRESS = "progress"
    QUERY_EXECUTION_TIME = "query_execution_time"
    RECORD_COUNT = "record_count"
    SAVE_RESULTS = "save_results"
    SEARCH_ID = "search_id"
    STATUS = "status"
    

class GetArielQueryResultsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "search_id": {
      "type": "string",
      "title": "Search ID",
      "description": "Search ID",
      "order": 1
    }
  },
  "required": [
    "search_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetArielQueryResultsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "compressed_data_file_count": {
      "type": "integer",
      "title": "Compressed Data File Count",
      "description": "Compressed data file count",
      "order": 11
    },
    "compressed_data_total_size": {
      "type": "integer",
      "title": "Compressed Data Total Size",
      "description": "Compressed data total size",
      "order": 15
    },
    "cursor_id": {
      "type": "string",
      "title": "Cursor ID",
      "description": "Cursor ID",
      "order": 13
    },
    "data_file_count": {
      "type": "integer",
      "title": "Data File Count",
      "description": "Data file count",
      "order": 12
    },
    "data_total_size": {
      "type": "integer",
      "title": "Data Total Size",
      "description": "Data total size",
      "order": 10
    },
    "desired_retention_time_msec": {
      "type": "integer",
      "title": "Desired Retention Time",
      "description": "Desired retention time in ms",
      "order": 4
    },
    "error_messages": {
      "type": "array",
      "title": "Error Messages",
      "description": "Error messages",
      "items": {
        "$ref": "#/definitions/error_messages"
      },
      "order": 7
    },
    "index_file_count": {
      "type": "integer",
      "title": "Index File Count",
      "description": "Index file count",
      "order": 16
    },
    "index_total_size": {
      "type": "integer",
      "title": "Index Total Size",
      "description": "Total size of index",
      "order": 5
    },
    "processed_record_count": {
      "type": "integer",
      "title": "Processed Record Count",
      "description": "Processed record count",
      "order": 6
    },
    "progress": {
      "type": "integer",
      "title": "Progress",
      "description": "Progress",
      "order": 14
    },
    "query_execution_time": {
      "type": "integer",
      "title": "Query Execution Time",
      "description": "Query execution time",
      "order": 2
    },
    "record_count": {
      "type": "integer",
      "title": "Record Count",
      "description": "Record count",
      "order": 3
    },
    "save_results": {
      "type": "boolean",
      "title": "Save Results",
      "description": "Save results",
      "order": 8
    },
    "search_id": {
      "type": "string",
      "title": "Search ID",
      "description": "ID of the search",
      "order": 9
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Status",
      "order": 1
    }
  },
  "definitions": {
    "error_messages": {
      "type": "object",
      "title": "error_messages",
      "properties": {
        "code": {
          "type": "string",
          "title": "Error Code",
          "description": "Error code",
          "order": 1
        },
        "contexts": {
          "type": "array",
          "title": "Error Context",
          "description": "Error Context",
          "items": {
            "type": "string"
          },
          "order": 2
        },
        "message": {
          "type": "string",
          "title": "Error Message",
          "description": "Error Message",
          "order": 3
        },
        "severity": {
          "type": "string",
          "title": "Error Severity",
          "description": "Error Severity",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
