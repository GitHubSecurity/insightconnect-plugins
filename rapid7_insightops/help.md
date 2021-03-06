
# Rapid7 InsightOps

## About

[Rapid 7 InsightOps](https://insightops.help.rapid7.com/docs) is a log management and monitoring solution.
This plugin utilizes [Rapid7 InsightOps API](https://insightops.help.rapid7.com/docs).

## Actions

### Query Logs

This action is used to retrieve logs from InsightOps service.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|logs|logs|True|None|

### Submit Log Data

This action is used to submit JSON to a specified log within an InsightOps logset.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|data|object|None|False|JSON that will be passed to InsightOps logset|None|
|logset_container_id|string|None|False|An UUID that specifics a container within an InsightOps logset|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Reports if data was submitted successfully|

### Create Logset Container

This action is used to create a container within the specified logset for the InsightOps service.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|le_agent_filename|string|None|False|Log entry agent filename|None|
|source_type|string|token|False|A unique identifier for the log|None|
|name|string|None|False|Name of the container|None|
|token_seed|string|None|False|Token Seed is used to generate a token that can be shared. If a random uuid needs to be created leave this blank|None|
|structures|[]string|None|False|The structure of the log. e.g. Syslog, JSON, Apache and Nginx|None|
|id|string|None|False|ID points to the [logset](https://insightops.help.rapid7.com/docs/using-log-search) ID to which the container will be created e.g. c17cef2e-01c1-404e-b42b-ea5088c2f713|None|
|le_agent_follow|string|None|False|Log entry agent follow|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|log|logset_container|False|Returned data from created container|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|log|post_log|False|Data returned from the posted log|

## Triggers

This plugin does not contain any triggers.

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|region|string|us|True|Region of InsightOps service to access e.g. eu|['eu', 'us']|
|api_key|string|None|True|API Key to access InsightOps service e.g. 39dd20eb-1337-45a0-a4044-133f237b50fa|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Create logset containers
* Submit JSON to logset containers
* Query for logs

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture
* 1.0.1 - Support web server mode | Use new credential types

## References

* [InsightOps](https://www.rapid7.com/products/insightops/m)
* [InsightOps API](https://insightops.help.rapid7.com/docs)
* [Logsets](https://insightops.help.rapid7.com/docs/using-log-search)
