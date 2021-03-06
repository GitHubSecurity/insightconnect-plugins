
# Awk

## About

[Awk](https://www.gnu.org/software/gawk/manual/gawk.html) is a pattern scanning and processing language. This plugin uses GNU Awk to manipulate input data.
For example, here's a simple example of Awk from the command line:

```

$ awk '{ print "Second column contents:",$2 }' 3columns.txt
Second column contents: dog
Second column contents: cat
Second column contents: horse
Second column contents: birds

```

## Actions

### Process String

This action can be used to process string with Awk.

#### Input

It accepts an Awk expression and a string to process. Awk's command-line options can be passed in the expression.
Single-quotes are required to enclose the program part of the expression. For example, invoking Awk with a
command-line option and a program: `-F , '{ print $2 }'`.

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|text|string|None|True|String to process|None|
|expression|string|None|True|Awk expression e.g. [pattern] { action }|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|out|string|False|Processed string|

### Process File

This action is used to process a file encoded data such as a file. The data is decoded and then ran through Awk.

#### Input

It accepts an Awk expression and file encoded data (file, string, etc.) to process.

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|expression|string|None|True|Awk expression e.g. [pattern] { action }|None|
|data|bytes|None|True|File to process|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|out|string|False|Processed string|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

By default, Awk returns a newline for each record. A common use case is to print a field from a body of text without
the ending newline so that it may be passed to other plugins in a Komand workflow. There's at least two ways to achieve this
by setting the ORS (Output Record Separator) variable to nothing e.g. `-v ORS= '{ print $1 }'` or `'BEGIN { ORS="" } { print $1 }'`.

## Workflows

Examples:

* Data format and extraction

## Versions

* 0.1.0 - Initial plugin
* 1.1.1 - SSL bug fix in SDK
* 1.1.2 - Update to v2 Python plugin architecture
* 1.2.0 - Support web server mode

## References

* [Awk](https://www.gnu.org/software/gawk/manual/gawk.html)
