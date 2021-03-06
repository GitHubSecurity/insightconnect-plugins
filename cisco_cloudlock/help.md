
# CloudLock

## About

[Cisco CloudLock](https://www.cisco_cloudlock.com) is the cloud-native CASB and Cloud Cybersecurity Platform
This plugin utilizes the [Cisco CloudLock API](https//api.cisco_cloudlock.com).

## Actions

### List All Suspicious IP Entries

This action is used to lists all suspicious IP entries.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|q|string|None|False|Match string|['Name', 'Location', 'IP Address', 'Categories']|
|limit|number|20|False|Number of paginated results to return. Max\: 100|None|
|name|string|None|False|Match a substring within entry name|None|
|offset|number|0|False|Pagination offset|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|entries|[]suspicious_ip_entry|False|None|

### List Entities

This action is used to list all asset list pages and exports.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|limit|number|20|False|Number of paginated results to return. Max\: 100|None|
|offset|number|0|False|Pagination offset|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|entities|[]entity|False|None|

### List All Organization Policies

This action is used to lists all of an organizations configured policies.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|state|string|None|False|State of the policy|['Active', 'Inactive']|
|limit|number|20|False|Number of paginated results to return. Max\: 100|None|
|offset|number|0|False|Pagination offset|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|policies|[]policy|False|None|

### List Activities

This action is used to lists the UBA (user behavioral analysis) activities.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|limit|number|20|False|Number of paginated results to return. Max\: 100|None|
|offset|number|0|False|Pagination offset|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|activities|[]activity|False|None|

### List All Incidents

This action is used to list all incidents triggered by the CloudLock policy engine.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|created_before|date|None|False|Created on start date look up period|None|
|limit|number|20|False|Number of paginated results to return. Max\: 100|None|
|severity|string|None|False|Severity level to search on|['INFO', 'WARNING', 'CRITICAL', 'ALERT']|
|created_after|date|None|False|Created on end date look up period. Example\: 2014-02-01|None|
|offset|number|0|False|Pagination offset|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incidents|[]incident|False|None|

### List All Organization Applications

This action is used to lists an organizations installed applications.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|limit|number|20|False|Number of paginated results to return. Max\: 100|None|
|classification|string|None|False|Classification type of the application|['Unclassified', 'Trusted', 'Restricted', 'Banned']|
|offset|number|0|False|Pagination offset|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|applications|[]application|False|None|

## Triggers

This plugin does not contain any triggers.

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|API key|None|

## Troubleshooting

No troubleshooting information.

## Workflows

Examples:

* View information about cloud applications used in the organization
* View cloud application users and events related to them
* CloudLock management

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types

## References

* [Cisco CloudLock](https://www.cloudlock.com)
