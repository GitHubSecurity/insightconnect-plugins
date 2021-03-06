# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ARCH = "arch"
    DISTRO = "distro"
    EPOCH = "epoch"
    KEY = "key"
    NAME = "name"
    RELEASE = "release"
    REPO = "repo"
    VERSION = "version"
    

class Output:
    ARCHITECTURE = "architecture"
    BUILD_DATE = "build_date"
    BUILD_HOST = "build_host"
    DESCRIPTION = "description"
    FILES = "files"
    FOUND = "found"
    LICENSE = "license"
    NAME = "name"
    PACKAGER = "packager"
    RELEASE = "release"
    RELOCATIONS = "relocations"
    SIGNATURE = "signature"
    SIZE = "size"
    SOURCE_RPM = "source_rpm"
    SUMMARY = "summary"
    URL = "url"
    VENDOR = "vendor"
    VERSION = "version"
    

class InfoInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "arch": {
      "type": "string",
      "title": "Architecture",
      "description": "System architecture",
      "enum": [
        "x86_64",
        "i686",
        "i386",
        "noarch"
      ],
      "order": 5
    },
    "distro": {
      "type": "string",
      "title": "Distribution",
      "description": "Distribution",
      "enum": [
        "CentOS 6",
        "CentOS 7",
        "Fedora 23",
        "Fedora 24",
        "Fedora 25",
        "Fedora 26"
      ],
      "order": 8
    },
    "epoch": {
      "type": "string",
      "title": "Epoch",
      "description": "Epoch",
      "order": 2
    },
    "key": {
      "type": "string",
      "title": "Key",
      "description": "GPG key URL",
      "order": 7
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Canonical package name",
      "order": 1
    },
    "release": {
      "type": "string",
      "title": "Release",
      "description": "Release version",
      "order": 4
    },
    "repo": {
      "type": "string",
      "title": "Repository",
      "description": "Repository URL",
      "order": 6
    },
    "version": {
      "type": "string",
      "title": "Version",
      "description": "Package version",
      "order": 3
    }
  },
  "required": [
    "distro",
    "name",
    "arch"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class InfoOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "architecture": {
      "type": "string",
      "title": "Architecture",
      "description": "System architecture",
      "order": 5
    },
    "build_date": {
      "type": "string",
      "title": "Build Date",
      "displayType": "date",
      "description": "Build date",
      "format": "date-time",
      "order": 9
    },
    "build_host": {
      "type": "string",
      "title": "Build Host",
      "description": "Build host",
      "order": 10
    },
    "description": {
      "type": "string",
      "title": "Description",
      "description": "Package description",
      "order": 16
    },
    "files": {
      "type": "array",
      "title": "Files",
      "description": "Package files",
      "items": {
        "$ref": "#/definitions/file"
      },
      "order": 18
    },
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "Package found",
      "order": 2
    },
    "license": {
      "type": "string",
      "title": "License",
      "description": "License",
      "order": 6
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Package name",
      "order": 1
    },
    "packager": {
      "type": "string",
      "title": "Packager",
      "description": "Packager",
      "order": 14
    },
    "release": {
      "type": "string",
      "title": "Release",
      "description": "Distro release",
      "order": 4
    },
    "relocations": {
      "type": "string",
      "title": "Relocations",
      "description": "Relocations",
      "order": 11
    },
    "signature": {
      "$ref": "#/definitions/signature",
      "title": "Signature",
      "description": "Signature",
      "order": 7
    },
    "size": {
      "type": "integer",
      "title": "Size",
      "description": "Package size",
      "order": 12
    },
    "source_rpm": {
      "type": "string",
      "title": "Source RPM",
      "description": "Source RPM",
      "order": 8
    },
    "summary": {
      "type": "string",
      "title": "Summary",
      "description": "Package summary",
      "order": 15
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "Package download URL",
      "order": 17
    },
    "vendor": {
      "type": "string",
      "title": "Vendor",
      "description": "Package vendor",
      "order": 13
    },
    "version": {
      "type": "string",
      "title": "Version",
      "description": "Package version",
      "order": 3
    }
  },
  "definitions": {
    "file": {
      "id": "file",
      "type": "object",
      "title": "File",
      "description": "File Object",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "description": "File contents",
          "format": "bytes"
        },
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of file"
        }
      }
    },
    "signature": {
      "type": "object",
      "title": "signature",
      "properties": {
        "key": {
          "type": "string",
          "title": "Hash",
          "order": 3
        },
        "scheme": {
          "type": "string",
          "title": "Scheme",
          "order": 1
        },
        "time": {
          "type": "string",
          "title": "Datetime of Last Hash",
          "displayType": "date",
          "format": "date-time",
          "order": 2
        }
      },
      "required": [
        "scheme",
        "time",
        "key"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
