
# Get URL

## About

The Get URL plugin allows you to download files from a URL. Supported protocols are HTTP, HTTPS, and FTP.

This plugin's cache is enabled across workflows to store previously downloaded files to reduce future web requests.
To reduce the number of subsequent requests the Etag and If-Modified-Since fields are also checked.

## Actions

### Get URL

This action is used to download the contents of a URL.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|URL to Download|None|
|checksum|string|None|False|Checksum verification (MD5, SHA1, SHA256)|None|
|is_verify|boolean|True|True|Validate certificate|None|
|timeout|integer|60|False|Timeout in seconds|None|

#### Output

This action returns the contents of the URL and an HTTP status code.

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|False|None|
|bytes|bytes|False|None|

## Triggers

### Poll URL

This trigger is used to monitor the contents of a URL for changes. The contents are returned when a change has been detected.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|URL to Download|None|
|poll|integer|60|False|Poll in seconds|None|
|is_verify|boolean|True|True|Validate certificate|None|

#### Output

This action returns the contents of the URL and an HTTP status code.

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|False|None|
|bytes|bytes|False|None|

## Connection

This plugin does not contain a connection.

## Troubleshooting

Some web servers do not support cache control mechanisms, or do not use them properly.

## Workflows

Examples:

* File submission

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Support web server mode

## References

* [Handling Last-Modified and ETag](http://www.diveintopython.net/http_web_services/etags.html)
