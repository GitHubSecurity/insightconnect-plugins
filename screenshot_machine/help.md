
# Screenshot Machine

## About

Capture screenshots using the [Screenshot Machine](https://screenshotmachine.com/) API

## Actions

### Capture URL Screenshot

This action is used to capture the screenshot of a URL and return a `file` object.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|URL to screenshot|None|
|cache_age_days|integer|0|False|Use Cached Image From X days ago. Enter in the age in days that will be accepted. 0 means do not use cache|[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]|
|size|string|tiny|False|Size string. Sizes are listed here\: https\://screenshotmachine.com/apiguide.php|['tiny', 'small', 'seminormal', 'normal', 'medium', 'large', 'extra_large', 'full', 'mobile_normal', 'mobile_full']|
|timeout|integer|200|False|Timeout in ms to wait for capture|[0, 200, 400, 600, 800, 1000]|
|format|string|JPG|False|Format|['JPG', 'PNG', 'GIF']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|False|URL Captured|
|screenshot|file|False|Screenshot Captured|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin requires an API key and a password.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|secret|string|None|False|Secret|None|
|key|string|None|True|API Key|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* [URL Screenshot](https://market.komand.com/snippets/ross/url-screenshot/1.0.0)
* Investigation enrichment
* Documentation

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Rename action to "Capture URL Screenshot"

## References

* [Screenshot Machine](https://screenshotmachine.com/)
* [API Guide](https://screenshotmachine.com/apiguide.php)
