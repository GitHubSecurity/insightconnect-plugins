
# Carbon Black Live Response

## About

[Carbon Black Live Response](https://developer.carbonblack.com/reference/cb-defense/1/live-response-api/) allows security operators to collect information and take action on remote endpoints in real time. These actions include the ability to upload, download, and remove files, retrieve and remove registry entries, dump contents of physical memory, execute and terminate processes.

## Actions

### Delete File

This action is used to delete a file from the endpoint.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hostname|string|None|True|Hostname of endpoint to start live session with|None|
|object_path|string|None|True|The source path of the object to delete|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Whether or not the deletion was successful|

## Triggers

This plugin does not contain any triggers.

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|https\://127.0.0.1/api/bit9platform/v1|True|Carbon Black Server API URL|None|
|verify_ssl|boolean|True|True|SSL Certificate Verification|None|
|api_key|credential_secret_key|None|True|API token found in your Carbon Black profile|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Delete malicious files off endpoints

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 0.1.2 - Update to v2 Python plugin architecture
* 0.1.3 - Bug fix for CI tool incorrectly uploading plugins
* 1.0.0 - Support web server mode

## References

* [Carbon Black Live Response](https://developer.carbonblack.com/reference/cb-defense/1/live-response-api/)
