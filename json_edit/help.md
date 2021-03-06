
# JSON Edit

## About

JSON Edit allows for the manipulation of JSON data.

## Actions

### Update

This action is used to update a value by key. It updates any values matching the key for an `object` or an `array` of `object`s.
A user must supply one of these data structure as input for the plugin to update.

It will iterate through each dictionary but is not recursive so nested dictionaries will not be operated on.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|array|[]object|None|False|Array of JSON objects|None|
|object|object|None|False|JSON object|None|
|key|string|None|True|JSON key to update|None|
|value|string|None|True|New value|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|json|[]object|True|Array of objects|

Example output:

```

{
  "json": [
    {
      "hostname": "BIGFIX-SRV",
      "ip": "Sanitized!",
      "os": "Win2012 6.2.9200"
    },
    {
      "hostname": "BIGFIX-DC",
      "ip": "Sanitized!",
      "os": "Win10"
    }
  ]
}

```

### Delete

This action is used to delete a key by name. It deletes any matching keys for an `object` or an `array` of `object`s.
A user must supply one of these data structure as input for the plugin to update.

It will iterate through each dictionary but is not recursive so nested dictionaries will not be operated on.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|array|[]object|None|False|Array of JSON objects|None|
|object|object|None|False|JSON object|None|
|key|string|None|True|Key to remove|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|json|[]object|True|Array of objects|

Example output:

```

{
  "json": [
    {
      "hostname": "BIGFIX-SRV",
      "os": "Win2012 6.2.9200"
    },
    {
      "hostname": "BIGFIX-DC",
      "os": "Win10 6.2.9200"
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

## Versions

* 1.0.0 - Initial plugin
* 1.0.1 - Add `utilities` plugin tag for Marketplace searchability

## Workflows

Examples:

* Update JSON reports
* Sanitize JSON fields

## References

* [JSON](https://www.json.org/)
