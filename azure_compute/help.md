
# Azure Compute

## About

[Microsoft Azure](https://azure.microsoft.com/) is a growing collection of integrated cloud services that developers and IT professionals
use to build, deploy, and manage applications through our global network of datacenters.

## Actions

### Stop a Virtual Machine

This action is used to stop a virtual machine.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Resource Group|string|None|True|The resource group that will contain the virtual machine|None|
|SubscriptionId|string|None|True|The identifier of your subscription|None|
|VM|string|None|True|The name of the virtual machine|None|
|API Version|string|2016-04-30-preview|True|The version of the API to use. The current version is 2016-04-30-preview|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Status Code|integer|False|HTTP status code|

### Get Virtual Machines Sizes in AvailabilitySet

This action is used to list available virtual machine sizes in an availability set.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Resource Group|string|None|True|The resource group that will contain the virtual machine|None|
|SubscriptionId|string|None|True|The identifier of your subscription|None|
|Availability Set|string|None|True|The availability set that contains the virtual machine|None|
|API Version|string|2016-04-30-preview|True|The version of the API to use. The current version is 2016-04-30-preview|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|value|[]object|False|List sizes in availability set|

### Get Information About a Virtual Machine

This action is used to get information about a virtual machine (model view and instance view).

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Resource Group|string|None|True|The resource group that will contain the virtual machine|None|
|SubscriptionId|string|None|True|The identifier of your subscription|None|
|VM|string|None|True|The name of the virtual machine|None|
|API Version|string|2016-04-30-preview|True|The version of the API to use. The current version is 2016-04-30-preview|None|
|Mode|string|modelViewAndInstanceView|False|This mode get information of model view or instance view or both|['modelView', 'instanceView', 'modelViewAndInstanceView']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Response|object|False|Response object|

### Generalize a Virtual Machine

This action is used to mark a virtual machine as generalized in Azure.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Resource Group|string|None|True|The resource group that will contain the virtual machine|None|
|SubscriptionId|string|None|True|The identifier of your subscription|None|
|VM|string|None|True|The name of the virtual machine|None|
|API Version|string|2016-04-30-preview|True|The version of the API to use. The current version is 2016-04-30-preview|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Status Code|integer|False|HTTP status code|

### Stop and Deallocate a Virtual Machine

This action is used to stop and deallocate a virtual machine.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Resource Group|string|None|True|The resource group that will contain the virtual machine|None|
|SubscriptionId|string|None|True|The identifier of your subscription|None|
|VM|string|None|True|The name of the virtual machine|None|
|API Version|string|2016-04-30-preview|True|The version of the API to use. The current version is 2016-04-30-preview|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Status Code|integer|False|HTTP status code|

### Capture Virtual Machine

This action is used to save an image of a virtual machine.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Resource Group|string|None|True|The resource group that will contain the virtual machine|None|
|DestinationContainerName|string|None|True|Specifies the name of the container inside which the vhds constituting the image resides|None|
|SubscriptionId|string|None|True|The identifier of your subscription|None|
|Overwrite Vhds|boolean|True|True|Specifies if an existing vhd with same prefix inside the destination container is overwritten|None|
|VM|string|None|True|The name of the virtual machine|None|
|API Version|string|2016-04-30-preview|True|The version of the API to use. The current version is 2016-04-30-preview|None|
|Vhd Prefix|string|None|True|Specifies the prefix in the name of the blobs that constitute the storage profile of the image|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Status Code|integer|False|HTTP status code|

### Virtual Machines in Subscription

This action is used to lists the virtual machines in a subscription.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|SubscriptionId|string|None|True|The identifier of your subscription|None|
|API Version|string|2016-04-30-preview|True|The version of the API to use. The current version is 2016-04-30-preview|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Value|[]object|False|List virtual machines in subscription|

### Virtual Machines Sizes

This action is used to list available virtual machine sizes for resizing.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Resource Group|string|None|True|The resource group that will contain the virtual machine|None|
|SubscriptionId|string|None|True|The identifier of your subscription|None|
|VM|string|None|True|The name of the virtual machine|None|
|API Version|string|2016-04-30-preview|True|The version of the API to use. The current version is 2016-04-30-preview|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Value|[]object|False|List sizes|

### List the Virtual Machines

This action is used to list the virtual machines in a resource group.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Resource Group|string|None|True|The resource group that will contain the virtual machine|None|
|SubscriptionId|string|None|True|The identifier of your subscription|None|
|API Version|string|2016-04-30-preview|True|The version of the API to use. The current version is 2016-04-30-preview|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Value|[]object|False|List items virtual machine in a resource group|

### Virtual Machines Sizes for Subscription

This action is used to lists available virtual machine sizes for a subscription.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|SubscriptionId|string|None|True|The identifier of your subscription|None|
|Location|string|None|True|The location of the virtual machine|None|
|API Version|string|2016-04-30-preview|True|The version of the API to use. The current version is 2016-04-30-preview|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Value|[]object|False|List sizes of location|

### Start a Virtual Machine

This action is used to start a virtual machine.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Resource Group|string|None|True|The resource group that will contain the virtual machine|None|
|SubscriptionId|string|None|True|The identifier of your subscription|None|
|VM|string|None|True|The name of the virtual machine|None|
|API Version|string|2016-04-30-preview|True|The version of the API to use. The current version is 2016-04-30-preview|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Status Code|integer|False|HTTP status code|

### Restart a Virtual Machine

This action is used to restart a virtual machine.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Resource Group|string|None|True|The resource group that will contain the virtual machine|None|
|SubscriptionId|string|None|True|The identifier of your subscription|None|
|VM|string|None|True|The name of the virtual machine|None|
|API Version|string|2016-04-30-preview|True|The version of the API to use. The current version is 2016-04-30-preview|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Status Code|integer|False|HTTP status code|

### Delete a Virtual Machine

This action is used to delete a virtual machine.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Resource Group|string|None|True|The resource group that will contain the virtual machine|None|
|SubscriptionId|string|None|True|The identifier of your subscription|None|
|VM|string|None|True|The name of the virtual machine|None|
|API Version|string|2016-04-30-preview|True|The version of the API to use. The current version is 2016-04-30-preview|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Status Code|integer|False|HTTP status code|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin requires network access to a Azure REST API server. Follow the [guide](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal)
to acquire the required connection information.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Client ID|string|None|True|The application id that the application registration portal assigned to your app|None|
|Client Secret|string|None|True|The application secret that you generated for your app in the app registration portal|None|
|Tenant ID|string|None|True|This is active directory id|None|
|API Version|string|2016-04-30-preview|True|The version of the API to use. The current version is 2016-04-30-preview|None|
|Host|string|https\://management.azure.com|True|Azure REST API Server|None|

## Troubleshooting

Error values use the standard HTTP codes (200 OK, 404 Not Found, etc)

## Workflows

Examples:

* Containment
* Machine management

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture
* 2.0.0 - Support web server mode | Update to new credential types | Rename "Get information about a virtual machine" to "Get Information About a Virtual Machine"

## References

* [Microsoft Azure](https://azure.microsoft.com/)
* [Azure Virtual Machines](https://docs.microsoft.com/en-us/rest/api/compute/virtualmachines)
