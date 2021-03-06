
# Nmap

## About

[Nmap](https://nmap.org) ("Network Mapper") is an open source tool for network exploration and security auditing.
The Nmap plugin runs Nmap directly and returns the results.

## Actions

### Scan

This action is used to run an Nmap scan.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sudo|boolean|False|True|Whether or not to use superuser privileges for scan|None|
|hosts|string|None|True|Host(s) to scan in Nmap-allowed formats|None|
|ports|string|None|False|Port(s) to scan in Nmap-allowed formats|None|
|arguments|string|None|False|Arguments to supply to the Nmap command, Nmap <arguments>|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|[]hosts|False|Scan results|

Example output:

```

{
  "result": [
    {
      "hostnames": [
        {}
      ],
      "addresses": {
        "ipv4": "192.168.1.100"
      },
      "vendor": {},
      "status": {
        "state": "up",
        "reason": "echo-reply"
      },
      "portused": [
        {
          "state": "closed",
          "proto": "tcp",
          "portid": "27"
        }
      ],
      "osmatch": [
        {
          "name": "Apple AirPort Extreme WAP",
          "accuracy": "98",
          "line": "3160",
          "osclass": [
            {
              "type": "WAP",
              "vendor": "Apple",
              "osfamily": "embedded",
              "accuracy": "98",
              "cpe": [
                "cpe:/h:apple:airport_extreme"
              ]
            }
          ]
        }
      ]
    }
  ]
}

```

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Port scanning
* Host discovery

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 0.2.0 - Update to v2 Python plugin architecture
* 1.0.0 - Overhaul with additional inputs and typed output
* 1.0.1 - Support web server mode

## References

* [Nmap](https://nmap.org/)
