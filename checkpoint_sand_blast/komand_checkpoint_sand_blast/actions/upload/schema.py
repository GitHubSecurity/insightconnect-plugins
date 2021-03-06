# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    FILE_BYTES = "file_bytes"
    FILE_NAME = "file_name"
    FILE_TYPE = "file_type"
    

class Output:
    RESULTS = "results"
    

class UploadInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file_bytes": {
      "type": "string",
      "title": "File Bytes",
      "displayType": "bytes",
      "description": "The file bytes",
      "format": "bytes",
      "order": 3
    },
    "file_name": {
      "type": "string",
      "title": "File Name",
      "description": "The name of the file",
      "order": 1
    },
    "file_type": {
      "type": "string",
      "title": "File Type",
      "description": "File extension e.g. docx, pdf, ect",
      "order": 2
    }
  },
  "required": [
    "file_name",
    "file_bytes"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UploadOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "$ref": "#/definitions/upload_response",
      "title": "Results",
      "description": "Results from the upload",
      "order": 1
    }
  },
  "definitions": {
    "images": {
      "type": "object",
      "title": "images",
      "properties": {
        "id": {
          "type": "string",
          "title": "Id",
          "order": 3
        },
        "report": {
          "$ref": "#/definitions/report",
          "title": "Report",
          "order": 1
        },
        "revision": {
          "type": "integer",
          "title": "Revision",
          "order": 4
        },
        "status": {
          "type": "string",
          "title": "Status",
          "order": 2
        }
      },
      "definitions": {
        "report": {
          "type": "object",
          "title": "report",
          "properties": {
            "verdict": {
              "type": "string",
              "title": "Verdict",
              "order": 1
            }
          }
        }
      }
    },
    "report": {
      "type": "object",
      "title": "report",
      "properties": {
        "verdict": {
          "type": "string",
          "title": "Verdict",
          "order": 1
        }
      }
    },
    "status": {
      "type": "object",
      "title": "status",
      "properties": {
        "code": {
          "type": "integer",
          "title": "Code",
          "order": 1
        },
        "label": {
          "type": "string",
          "title": "Label",
          "order": 2
        },
        "message": {
          "type": "string",
          "title": "Message",
          "order": 3
        }
      }
    },
    "threat_emulation": {
      "type": "object",
      "title": "threat_emulation",
      "properties": {
        "combined_verdict": {
          "type": "string",
          "title": "Combined Verdict",
          "order": 3
        },
        "images": {
          "type": "array",
          "title": "Images",
          "items": {
            "$ref": "#/definitions/images"
          },
          "order": 2
        },
        "score": {
          "type": "integer",
          "title": "Score",
          "order": 4
        },
        "status": {
          "$ref": "#/definitions/status",
          "title": "Status",
          "order": 5
        },
        "trust": {
          "type": "integer",
          "title": "Trust",
          "order": 1
        }
      },
      "definitions": {
        "images": {
          "type": "object",
          "title": "images",
          "properties": {
            "id": {
              "type": "string",
              "title": "Id",
              "order": 3
            },
            "report": {
              "$ref": "#/definitions/report",
              "title": "Report",
              "order": 1
            },
            "revision": {
              "type": "integer",
              "title": "Revision",
              "order": 4
            },
            "status": {
              "type": "string",
              "title": "Status",
              "order": 2
            }
          },
          "definitions": {
            "report": {
              "type": "object",
              "title": "report",
              "properties": {
                "verdict": {
                  "type": "string",
                  "title": "Verdict",
                  "order": 1
                }
              }
            }
          }
        },
        "report": {
          "type": "object",
          "title": "report",
          "properties": {
            "verdict": {
              "type": "string",
              "title": "Verdict",
              "order": 1
            }
          }
        },
        "status": {
          "type": "object",
          "title": "status",
          "properties": {
            "code": {
              "type": "integer",
              "title": "Code",
              "order": 1
            },
            "label": {
              "type": "string",
              "title": "Label",
              "order": 2
            },
            "message": {
              "type": "string",
              "title": "Message",
              "order": 3
            }
          }
        }
      }
    },
    "upload_response": {
      "type": "object",
      "title": "upload_response",
      "properties": {
        "features": {
          "type": "array",
          "title": "Features",
          "items": {
            "type": "string"
          },
          "order": 5
        },
        "file_name": {
          "type": "string",
          "title": "File Name",
          "order": 4
        },
        "file_type": {
          "type": "string",
          "title": "File Type",
          "order": 3
        },
        "md5": {
          "type": "string",
          "title": "Md5",
          "order": 2
        },
        "status": {
          "$ref": "#/definitions/status",
          "title": "Status",
          "order": 1
        },
        "te": {
          "$ref": "#/definitions/threat_emulation",
          "title": "Te",
          "order": 6
        }
      },
      "definitions": {
        "images": {
          "type": "object",
          "title": "images",
          "properties": {
            "id": {
              "type": "string",
              "title": "Id",
              "order": 3
            },
            "report": {
              "$ref": "#/definitions/report",
              "title": "Report",
              "order": 1
            },
            "revision": {
              "type": "integer",
              "title": "Revision",
              "order": 4
            },
            "status": {
              "type": "string",
              "title": "Status",
              "order": 2
            }
          },
          "definitions": {
            "report": {
              "type": "object",
              "title": "report",
              "properties": {
                "verdict": {
                  "type": "string",
                  "title": "Verdict",
                  "order": 1
                }
              }
            }
          }
        },
        "report": {
          "type": "object",
          "title": "report",
          "properties": {
            "verdict": {
              "type": "string",
              "title": "Verdict",
              "order": 1
            }
          }
        },
        "status": {
          "type": "object",
          "title": "status",
          "properties": {
            "code": {
              "type": "integer",
              "title": "Code",
              "order": 1
            },
            "label": {
              "type": "string",
              "title": "Label",
              "order": 2
            },
            "message": {
              "type": "string",
              "title": "Message",
              "order": 3
            }
          }
        },
        "threat_emulation": {
          "type": "object",
          "title": "threat_emulation",
          "properties": {
            "combined_verdict": {
              "type": "string",
              "title": "Combined Verdict",
              "order": 3
            },
            "images": {
              "type": "array",
              "title": "Images",
              "items": {
                "$ref": "#/definitions/images"
              },
              "order": 2
            },
            "score": {
              "type": "integer",
              "title": "Score",
              "order": 4
            },
            "status": {
              "$ref": "#/definitions/status",
              "title": "Status",
              "order": 5
            },
            "trust": {
              "type": "integer",
              "title": "Trust",
              "order": 1
            }
          },
          "definitions": {
            "images": {
              "type": "object",
              "title": "images",
              "properties": {
                "id": {
                  "type": "string",
                  "title": "Id",
                  "order": 3
                },
                "report": {
                  "$ref": "#/definitions/report",
                  "title": "Report",
                  "order": 1
                },
                "revision": {
                  "type": "integer",
                  "title": "Revision",
                  "order": 4
                },
                "status": {
                  "type": "string",
                  "title": "Status",
                  "order": 2
                }
              },
              "definitions": {
                "report": {
                  "type": "object",
                  "title": "report",
                  "properties": {
                    "verdict": {
                      "type": "string",
                      "title": "Verdict",
                      "order": 1
                    }
                  }
                }
              }
            },
            "report": {
              "type": "object",
              "title": "report",
              "properties": {
                "verdict": {
                  "type": "string",
                  "title": "Verdict",
                  "order": 1
                }
              }
            },
            "status": {
              "type": "object",
              "title": "status",
              "properties": {
                "code": {
                  "type": "integer",
                  "title": "Code",
                  "order": 1
                },
                "label": {
                  "type": "string",
                  "title": "Label",
                  "order": 2
                },
                "message": {
                  "type": "string",
                  "title": "Message",
                  "order": 3
                }
              }
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
