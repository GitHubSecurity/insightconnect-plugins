
# Netmiko

## About

[Netmiko](https://www.api.netmiko.com) is a network device configuration tool that sends commands over SSHv2.  Netmiko is a fork of Paramiko.

## Actions

### Execute Configuration Commands

This action is used to change the device's configuration (global configuration mode).

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host|string|None|False|(Optional) Hosts to run remote commands.  If not provided, the connection host will be used|None|
|command|[]string|None|True|Commands to change the configuration on network device|["interface vlan 1","ip address 192.168.1.1"]|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|string|True|None|

Example Output:

```

{
  "results": "config term\n\nciscoasa(config)# ?\n\n.."
}

```

### Execute Show Commands

This action is used to check the devices configurations (privilege exec mode).

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host|string|None|False|(Optional) Host to run remote commands. If not provided, the connection host will be used|None|
|command|string|None|True|Show command to execute on network device|"show running-config"|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|string|True|None|

Example output:

```

{
  "results": "Interface Vlan1 \"inside\", is down, line protocol is down\n..."
}

```

## Triggers

This plugin does not contain any triggers.

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|secret|credential_secret_key|None|False|Secret password|None|
|verbose|boolean|False|True|Additional messages to standard output|None|
|key|credential_asymmetric_key|None|False|A base64 encoded SSH private key to use to authenticate to network device|None|
|device_type|string|None|True|Device type|['a10', 'accedian', 'alcatel_aos', 'alcatel_sros', 'arista_eos', 'aruba_os', 'avaya_ers', 'avaya_vsp', 'brocade_fastiron', 'brocade_netiron', 'brocade_nos', 'brocade_vdx', 'brocade_vyos', 'checkpoint_gaia', 'calix_b6', 'ciena_saos', 'cisco_asa', 'cisco_ios', 'cisco_nxos', 'cisco_s300', 'cisco_tp', 'cisco_wlc', 'cisco_xe', 'cisco_xr', 'coriant', 'dell_force10', 'dell_powerconnect', 'eltex', 'enterasys', 'extreme', 'extreme_wing', 'f5_ltm', 'fortinet', 'generic_termserver', 'hp_comware', 'hp_procurve', 'huawei', 'juniper', 'juniper_junos', 'linux', 'mellanox', 'mrv_optiswitch', 'netapp_cdot', 'ovs_linux', 'paloalto_panos', 'pluribus', 'quanta_mesh', 'ruckus_fastiron', 'ubiquiti_edge', 'ubiquiti_edgeswitch', 'vyatta_vyos', 'vyos']|
|credentials|credential_username_password|None|True|User to run commands as|None|
|host|string|None|True|Remote Host|None|
|port|integer|22|True|Remote port|None|

## Supported Devices

### Regularly Tested

* Arista vEOS
* Cisco ASA
* Cisco IOS
* Cisco IOS-XE
* Cisco IOS-XR
* Cisco NX-OS
* Cisco SG300
* HP Comware7
* HP ProCurve
* Juniper Junos
* Linux

### Limited Testing

* Alcatel AOS6/AOS8
* Avaya ERS
* Avaya VSP
* Brocade VDX
* Brocade ICX/FastIron
* Brocade MLX/NetIron
* Cisco WLC
* Dell-Force10 DNOS9
* Dell PowerConnect
* Huawei
* Mellanox
* Palo Alto PAN-OS
* Pluribus
* Ubiquiti EdgeSwitch Vyatta VyOS

### Experimental

* A10
* Accedian
* Alcatel-Lucent SR-OS
* Aruba
* Ciena SAOS
* Cisco Telepresence
* CheckPoint Gaia
* Enterasys
* Extreme EXOS
* Extreme Wing
* F5 LTM
* Fortinet
* MRV Communications OptiSwitch

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Versions

* 0.1.0 - Initial plugin
* 1.0.0 - Support web server mode | Update to new credential types | Rename "Execute show commands" action to "Execute Show Commands" | Rename "Execute configuration change commands" action to "Execute Configuration Commands"

## Workflows

* Configure network devices
* Show the network devices' running-configuration
* Update firewall rules

## References

* [Netmiko](https://github.com/ktbyers/netmiko)
* [Paramiko](http://www.paramiko.org/)
