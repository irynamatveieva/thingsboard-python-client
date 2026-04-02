
# DeviceProfile

`tb_paas_client.models.DeviceProfile`

A JSON value representing the device profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**DeviceProfileId**](DeviceProfileId.md) | JSON object with the device profile Id. Specify this field to update the device profile. Referencing non-existing device profile Id will cause error. Omit this field to create new device profile. | [optional] |
| **created_time** | **int** | Timestamp of the profile creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id that owns the profile. | [optional] [readonly] |
| **name** | **str** | Unique Device Profile Name in scope of Tenant. | [optional] |
| **description** | **str** | Device Profile description.  | [optional] |
| **image** | **str** | Either URL or Base64 data of the icon. Used in the mobile application to visualize set of device profiles in the grid view.  | [optional] |
| **type** | [**DeviceProfileType**](DeviceProfileType.md) | Type of the profile. Always 'DEFAULT' for now. Reserved for future use. | [optional] |
| **transport_type** | [**DeviceTransportType**](DeviceTransportType.md) | Type of the transport used to connect the device. Default transport supports HTTP, CoAP and MQTT. | [optional] |
| **provision_type** | [**DeviceProfileProvisionType**](DeviceProfileProvisionType.md) | Provisioning strategy. | [optional] |
| **default_rule_chain_id** | [**RuleChainId**](RuleChainId.md) | Reference to the rule chain. If present, the specified rule chain will be used to process all messages related to device, including telemetry, attribute updates, etc. Otherwise, the root rule chain will be used to process those messages. | [optional] |
| **default_dashboard_id** | [**DashboardId**](DashboardId.md) | Reference to the dashboard. Used in the mobile application to open the default dashboard when user navigates to device details. | [optional] |
| **default_queue_name** | **str** | Rule engine queue name. If present, the specified queue will be used to store all unprocessed messages related to device, including telemetry, attribute updates, etc. Otherwise, the 'Main' queue will be used to store those messages. | [optional] |
| **profile_data** | [**DeviceProfileData**](DeviceProfileData.md) | Complex JSON object that includes addition device profile configuration (transport, alarm rules, etc). | [optional] |
| **provision_device_key** | **str** | Unique provisioning key used by 'Device Provisioning' feature. | [optional] |
| **firmware_id** | [**OtaPackageId**](OtaPackageId.md) | Reference to the firmware OTA package. If present, the specified package will be used as default device firmware.  | [optional] |
| **software_id** | [**OtaPackageId**](OtaPackageId.md) | Reference to the software OTA package. If present, the specified package will be used as default device software.  | [optional] |
| **default_edge_rule_chain_id** | [**RuleChainId**](RuleChainId.md) | Reference to the edge rule chain. If present, the specified edge rule chain will be used on the edge to process all messages related to device, including telemetry, attribute updates, etc. Otherwise, the edge root rule chain will be used to process those messages. | [optional] |
| **version** | **int** |  | [optional] |
| **default** | **bool** | Used to mark the default profile. Default profile is used when the device profile is not specified during device creation. | [optional] |



## Referenced Types

> **EntityId types** (`DashboardId`, `DeviceProfileId`, `OtaPackageId`, `RuleChainId`, `TenantId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### DeviceProfileType (enum)
`DEFAULT`

#### DeviceTransportType (enum)
`DEFAULT` | `MQTT` | `COAP` | `LWM2M` | `SNMP`

#### DeviceProfileProvisionType (enum)
`DISABLED` | `ALLOW_CREATE_NEW_DEVICES` | `CHECK_PRE_PROVISIONED_DEVICES` | `X509_CERTIFICATE_CHAIN`

#### DeviceProfileData
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| configuration | DeviceProfileConfiguration | JSON object of device profile configuration | [optional] |
| transport_configuration | DeviceProfileTransportConfiguration | JSON object of device profile transport configuration | [optional] |
| provision_configuration | DeviceProfileProvisionConfiguration | JSON object of provisioning strategy type per device profile | [optional] |
| alarms | List[DeviceProfileAlarm] |  | [optional] |

#### DeviceProfileConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### DeviceProfileTransportConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### DeviceProfileProvisionConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| provision_device_secret | str | Provision device secret | [optional] |
| type | str |  |  |

#### DeviceProfileAlarm
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | str | String value representing the alarm rule id | [optional] |
| alarm_type | str | String value representing type of the alarm | [optional] |
| create_rules | Dict[str, AlarmRule] | Complex JSON object representing create alarm rules. The unique create alarm rule can be created for each alarm severity type. There can be 5 create alarm rules configured per a single alarm type. See method implementation notes and AlarmRule model for more details | [optional] |
| clear_rule | AlarmRule | JSON object representing clear alarm rule | [optional] |
| propagate | bool | Propagation flag to specify if alarm should be propagated to parent entities of alarm originator | [optional] |
| propagate_to_owner | bool | Propagation flag to specify if alarm should be propagated to the owner (tenant or customer) of alarm originator | [optional] |
| propagate_to_owner_hierarchy | bool | Propagation flag to specify if alarm should be propagated to the owner (tenant or customer) and all parent owners in the customer hierarchy | [optional] |
| propagate_to_tenant | bool | Propagation flag to specify if alarm should be propagated to the tenant entity | [optional] |
| propagate_relation_types | List[str] | JSON array of relation types that should be used for propagation. By default, 'propagateRelationTypes' array is empty which means that the alarm will be propagated based on any relation type to parent entities. This parameter should be used only in case when 'propagate' parameter is set to true, otherwise, 'propagateRelationTypes' array will be ignored. | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

#### AlarmRule
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| condition | AlarmCondition | JSON object representing the alarm rule condition | [optional] |
| alarm_details | str | String value representing the additional details for an alarm rule | [optional] |
| dashboard_id | DashboardId | JSON object with the dashboard Id representing the reference to alarm details dashboard used by mobile application | [optional] |
| schedule | AlarmSchedule | JSON object representing time interval during which the rule is active | [optional] |

#### AlarmCondition
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| condition | List[AlarmConditionFilter] |  | [optional] |
| spec | AlarmConditionSpec | JSON object representing alarm condition type | [optional] |

#### AlarmSchedule
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| dynamic_value | DynamicValueString |  | [optional] |
| type | AlarmScheduleType |  | [optional] |

#### AlarmConditionFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| value_type | EntityKeyValueType | String representation of the type of the value | [optional] |
| key | AlarmConditionFilterKey | JSON object for specifying alarm condition by specific key | [optional] |
| predicate | KeyFilterPredicate | JSON object representing filter condition | [optional] |
| value | object |  | [optional] |

#### AlarmConditionSpec
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### DynamicValueString
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| resolved_value | str |  | [optional] |
| source_type | DynamicValueSourceType |  | [optional] |
| source_attribute | str |  | [optional] |
| inherit | bool |  | [optional] |

#### AlarmScheduleType (enum)
`ANY_TIME` | `SPECIFIC_TIME` | `CUSTOM`

#### EntityKeyValueType (enum)
`STRING` | `NUMERIC` | `BOOLEAN` | `DATE_TIME`

#### AlarmConditionFilterKey
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | AlarmConditionKeyType | The key type | [optional] |
| key | str | String value representing the key | [optional] |

#### KeyFilterPredicate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### DynamicValueSourceType (enum)
`CURRENT_TENANT` | `CURRENT_CUSTOMER` | `CURRENT_USER` | `CURRENT_DEVICE`

#### AlarmConditionKeyType (enum)
`ATTRIBUTE` | `TIME_SERIES` | `ENTITY_FIELD` | `CONSTANT`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeviceProfile.model_validate(data)` or `DeviceProfile.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

